# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common utilities for running predictions."""
import base64
import collections
from contextlib import contextmanager
import logging
import os
import pickle
import subprocess
import sys
import time
import timeit
from ._interfaces import Model
import six


# --------------------------
# prediction.common
# --------------------------
ENGINE = "Prediction-Engine"
ENGINE_RUN_TIME = "Prediction-Engine-Run-Time"
FRAMEWORK = "Framework"
SCIKIT_LEARN_FRAMEWORK_NAME = "scikit_learn"
SK_XGB_FRAMEWORK_NAME = "sk_xgb"
XGBOOST_FRAMEWORK_NAME = "xgboost"
TENSORFLOW_FRAMEWORK_NAME = "tensorflow"
PREPROCESS_TIME = "Prediction-Preprocess-Time"
POSTPROCESS_TIME = "Prediction-Postprocess-Time"

# Default model names
DEFAULT_MODEL_FILE_NAME_JOBLIB = "model.joblib"
DEFAULT_MODEL_FILE_NAME_PICKLE = "model.pkl"

# Additional TF keyword arguments
INPUTS_KEY = "inputs"
OUTPUTS_KEY = "outputs"
SIGNATURE_KEY = "signature_name"

# Stats
COLUMNARIZE_TIME = "Prediction-Columnarize-Time"
UNALIAS_TIME = "Prediction-Unalias-Time"
ENCODE_TIME = "Prediction-Encode-Time"
SESSION_RUN_TIME = "Prediction-Session-Run-Time"
ALIAS_TIME = "Prediction-Alias-Time"
ROWIFY_TIME = "Prediction-Rowify-Time"
# TODO(b/67586901): Consider removing INPUT_PROCESSING_TIME during cleanup.
SESSION_RUN_ENGINE_NAME = "TF_SESSION_RUN"

# Location of where model files are copied locally.
LOCAL_MODEL_PATH = "/tmp/model"

PredictionErrorType = collections.namedtuple(
    "PredictionErrorType", ("message", "code"))


class PredictionError(Exception):
  """Customer exception for known prediction exception."""

  # The error code for prediction.
  FAILED_TO_LOAD_MODEL = PredictionErrorType(
      message="Failed to load model", code=0)
  INVALID_INPUTS = PredictionErrorType("Invalid inputs", code=1)
  FAILED_TO_RUN_MODEL = PredictionErrorType(
      message="Failed to run the provided model", code=2)
  INVALID_OUTPUTS = PredictionErrorType(
      message="There was a problem processing the outputs", code=3)
  INVALID_USER_CODE = PredictionErrorType(
      message="There was a problem processing the user code", code=4)
  # When adding new exception, please update the ERROR_MESSAGE_ list as well as
  # unittest.

  def __init__(self, error_code, error_detail, *args):
    super(PredictionError, self).__init__(error_code, error_detail, *args)

  @property
  def error_code(self):
    return self.args[0].code

  @property
  def error_message(self):
    return self.args[0].message

  @property
  def error_detail(self):
    return self.args[1]

  def __str__(self):
    return ("%s: %s (Error code: %d)" % (self.error_message,
                                         self.error_detail, self.error_code))


MICRO = 1000000
MILLI = 1000


class Timer(object):
  """Context manager for timing code blocks.

  The object is intended to be used solely as a context manager and not
  as a general purpose object.

  The timer starts when __enter__ is invoked on the context manager
  and stopped when __exit__ is invoked. After __exit__ is called,
  the duration properties report the amount of time between
  __enter__ and __exit__ and thus do not change. However, if any of the
  duration properties are called between the call to __enter__ and __exit__,
  then they will return the "live" value of the timer.

  If the same Timer object is re-used in multiple with statements, the values
  reported will reflect the latest call. Do not use the same Timer object in
  nested with blocks with the same Timer context manager.

  Example usage:

    with Timer() as timer:
      foo()
    print(timer.duration_secs)
  """

  def __init__(self, timer_fn=None):
    self.start = None
    self.end = None
    self._get_time = timer_fn or timeit.default_timer

  def __enter__(self):
    self.end = None
    self.start = self._get_time()
    return self

  def __exit__(self, exc_type, value, traceback):
    self.end = self._get_time()
    return False

  @property
  def seconds(self):
    now = self._get_time()
    return (self.end or now) - (self.start or now)

  @property
  def microseconds(self):
    return int(MICRO * self.seconds)

  @property
  def milliseconds(self):
    return int(MILLI * self.seconds)


class Stats(dict):
  """An object for tracking stats.

  This class is dict-like, so stats are accessed/stored like so:

    stats = Stats()
    stats["count"] = 1
    stats["foo"] = "bar"

  This class also facilitates collecting timing information via the
  context manager obtained using the "time" method. Reported timings
  are in microseconds.

  Example usage:

    with stats.time("foo_time"):
      foo()
    print(stats["foo_time"])
  """

  @contextmanager
  def time(self, name, timer_fn=None):
    with Timer(timer_fn) as timer:
      yield timer
    self[name] = timer.microseconds


class BaseModel(Model):
  """The base definition of an internal Model interface.
  """

  def __init__(self, client):
    """Constructs a BaseModel.

    Args:
      client: An instance of PredictionClient for performing prediction.
    """
    self._client = client
    self._user_processor = None

  def preprocess(self, instances, stats=None, **kwargs):
    """Runs the preprocessing function on the instances.

    Args:
      instances: list of instances as provided to the predict() method.
      stats: Stats object for recording timing information.
      **kwargs: Additional keyword arguments for preprocessing.

    Returns:
      A new list of preprocessed instances. Each instance is as described
      in the predict() method.
    """
    pass

  def postprocess(self, predicted_output, original_input=None, stats=None,
                  **kwargs):
    """Runs the postprocessing function on the instances.

    Args:
      predicted_output: list of instances returned by the predict() method on
        preprocessed instances.
      original_input: List of instances, before any pre-processing was applied.
      stats: Stats object for recording timing information.
      **kwargs: Additional keyword arguments for postprocessing.

    Returns:
      A new list of postprocessed instances.
    """
    pass

  def predict(self, instances, stats=None, **kwargs):
    """Runs preprocessing, predict, and postprocessing on the input."""

    stats = stats or Stats()
    self._validate_kwargs(kwargs)

    with stats.time(PREPROCESS_TIME):
      preprocessed = self.preprocess(instances, stats=stats, **kwargs)
    with stats.time(ENGINE_RUN_TIME):
      predicted_outputs = self._client.predict(
          preprocessed, stats=stats, **kwargs)
    with stats.time(POSTPROCESS_TIME):
      postprocessed = self.postprocess(
          predicted_outputs, original_input=instances, stats=stats, **kwargs)
    return postprocessed

  def _validate_kwargs(self, kwargs):
    """Validates and sets defaults for extra predict keyword arguments.

    Modifies the keyword args dictionary in-place. Keyword args will be included
    into pre/post-processing and the client predict method.
    Can raise Exception to error out of request on bad keyword args.
    If no additional args are required, pass.

    Args:
      kwargs: Dictionary (str->str) of keyword arguments to check.
    """
    pass


def decode_base64(data):
  if isinstance(data, list):
    return [decode_base64(val) for val in data]
  elif isinstance(data, dict):
    if six.viewkeys(data) == {"b64"}:
      return base64.b64decode(data["b64"])
    else:
      return {k: decode_base64(v) for k, v in six.iteritems(data)}
  else:
    return data


def copy_model_to_local(gcs_path, dest_path):
  """Copy files from gcs to a local path.

  Copies files directly to the dest_path.
  Sample behavior:
  dir1/
    file1
    file2
    dir2/
      file3

  copy_model_to_local("dir1", "/tmp")
  After copy:
  tmp/
    file1
    file2
    dir2/
      file3

  Args:
    gcs_path: Source GCS path that we're copying from.
    dest_path: Destination local path that we're copying to.

  Raises:
    Exception: If gsutil is not found.
  """
  copy_start_time = time.time()
  logging.debug("Starting to copy files from %s to %s", gcs_path, dest_path)
  if not os.path.exists(dest_path):
    os.makedirs(dest_path)
  gcs_path = os.path.join(gcs_path, "*")
  try:
    # Removed parallel downloads ("-m") because it was not working well in
    # gVisor (b/37269226).
    subprocess.check_call([
        "gsutil", "cp", "-R", gcs_path, dest_path], stdin=subprocess.PIPE)
  except subprocess.CalledProcessError as e:
    logging.error(str(e))
    raise
  logging.debug("Files copied from %s to %s: took %f seconds", gcs_path,
                dest_path, time.time() - copy_start_time)


def load_joblib_or_pickle_model(model_path):
  """Loads either a .joblib or .pkl file from GCS or from local.

  Loads one of DEFAULT_MODEL_FILE_NAME_JOBLIB or DEFAULT_MODEL_FILE_NAME_PICKLE
  files if they exist. This is used for both sklearn and xgboost.

  Arguments:
    model_path: The path to the directory that contains the model file. This
      path can be either a local path or a GCS path.

  Raises:
    PredictionError: If there is a problem while loading the file.

  Returns:
    A loaded scikit-learn or xgboost predictor object or None if neither
    DEFAULT_MODEL_FILE_NAME_JOBLIB nor DEFAULT_MODEL_FILE_NAME_PICKLE files are
    found.
  """
  if model_path.startswith("gs://"):
    copy_model_to_local(model_path, LOCAL_MODEL_PATH)
    model_path = LOCAL_MODEL_PATH

  try:
    model_file_name_joblib = os.path.join(model_path,
                                          DEFAULT_MODEL_FILE_NAME_JOBLIB)
    model_file_name_pickle = os.path.join(model_path,
                                          DEFAULT_MODEL_FILE_NAME_PICKLE)
    if os.path.exists(model_file_name_joblib):
      model_file_name = model_file_name_joblib
      try:
        # Load joblib only when needed. If we put this at the top, we need to
        # add a dependency to sklearn anywhere that prediction_lib is called.
        from sklearn.externals import joblib  # pylint: disable=g-import-not-at-top
      except Exception as e:
        error_msg = "Could not import sklearn module."
        logging.critical(error_msg)
        raise PredictionError(PredictionError.FAILED_TO_LOAD_MODEL, error_msg)

      logging.info("Loading model %s using joblib.", model_file_name)
      return joblib.load(model_file_name)

    elif os.path.exists(model_file_name_pickle):
      model_file_name = model_file_name_pickle
      logging.info("Loading model %s using pickle.", model_file_name)
      with open(model_file_name, "rb") as f:
        return pickle.loads(f.read())

    return None

  except Exception as e:
    raw_error_msg = str(e)
    if "unsupported pickle protocol" in raw_error_msg:
      error_msg = (
          "Could not load the model: {}. {}. Please make sure the model was "
          "exported using python {}. Otherwise, please specify the correct "
          "'python_version' parameter when deploying the model.").format(
              model_file_name, raw_error_msg, sys.version_info[0])
    else:
      error_msg = "Could not load the model: {}. {}.".format(
          model_file_name, raw_error_msg)
    logging.critical(error_msg)
    raise PredictionError(PredictionError.FAILED_TO_LOAD_MODEL, error_msg)


def detect_sk_xgb_framework_from_obj(model_obj):
  """Distinguish scikit-learn and xgboost using model object.

  Arguments:
    model_obj: A loaded model object

  Raises:
    PredictionError: If there is a problem detecting framework from object.

  Returns:
    Either scikit-learn framework or xgboost framework
  """
  # detect framework type from model object
  if "sklearn" in type(model_obj).__module__:
    return SCIKIT_LEARN_FRAMEWORK_NAME
  elif "xgboost" in type(model_obj).__module__:
    return XGBOOST_FRAMEWORK_NAME
  else:
    error_msg = (
        "Invalid model type detected: {}.{}. "
        "Please make sure the model file is an exported sklearn model, "
        "xgboost model or pipeline.").format(
            type(model_obj).__module__,
            type(model_obj).__name__)
    logging.critical(error_msg)
    raise PredictionError(PredictionError.FAILED_TO_LOAD_MODEL, error_msg)