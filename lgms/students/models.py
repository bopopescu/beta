from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.urls import reverse
import django.utils.timezone
from datetime import date
from crispy_forms.helper import FormHelper
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
#signals import
from django.db.models.signals import post_save

#import of star MyRating
from star_ratings.models import Rating, AbstractBaseRating
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

#to aggregate
from django.db.models import Avg, Max, Sum, Min

from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _




class CustomUser(AbstractUser):

    # user_type_choices = {
    # (1, 'Parents' ),
    # (2, 'Teacher' ),
    # (3, 'Admin'),
    #
    # }
    # user_type = models.PositiveSmallIntegerField(choices=user_type_choices, help_text='Choose User Role')

    ### this is for the user choices
    is_parent = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField('Username', max_length=64, unique=True)
    first_name = models.CharField('First Name', blank=True, max_length=64)
    email = models.EmailField(unique=True)
    last_name = models.CharField('Last Name', blank=True, max_length=64)
    address = models.CharField('Full Address', max_length=300, blank=True)
    dateofbirth = models.DateField('Date of Birth', default=date.today)
    dateuserjoined = models.DateTimeField('Date Registered', default=django.utils.timezone.now)
    dateupdatedbio = models.DateTimeField('Date Updated', default=django.utils.timezone.now)
    mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    homenumber = PhoneNumberField('Landline Number', blank=True, help_text='landline : +6328888888')
    profilepic = models.ImageField('Profile Picture',upload_to='profile_image', blank=True)


    civilstats = {
        ('M', 'Married'),
        ('SP', 'Single Parent'),
        ('D', 'Divorcee'),
        ('W', 'Widowed'),
    }

    civilstatus = models.CharField(max_length=20, choices=civilstats, blank=True, default='M', help_text="Please select Civit Status")

    religionchoices = {

        ('C', 'Catholic'),
        ('B', 'Buddhist'),
        ('M', 'Muslim'),
        ('I', 'INC'),
    }

    religion = models.CharField(max_length=30, choices=religionchoices, blank=True, default='C', help_text="Please select Religion")
    #code for saving user to specific


    # def add_view()
    def __str__(self):
        return '%s' % (self.email)

    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('LGMS User Database')

    class Meta:
        ordering = ['username']


# commented for the meantime -- 01 dec 2018s
#
# def create_customuser(sender, **kwargs):
#     if kwargs['created']:
#         custom_userprofile = CustomUser.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_customuser, sender=User)


# class ParentsInfo(models.Model):
#     mothersname = models.ForeignKey('CustomUser', max_length=30, on_delete=models.CASCADE, related_name="customuser_fathersname", verbose_name="Mothers Name")
#     fathersname = models.ForeignKey('CustomUser', max_length=30, on_delete=models.CASCADE, related_name="customuser_mothersname", verbose_name="Fathers Name")
#     guardiansname = models.CharField('Guardians Name', max_length=64, blank=True)
#     address = models.CharField('Home Address', max_length=64)
#     email = models.EmailField('Email Address', max_length=64,default='example@email.com')
#
#     mobilenumber = PhoneNumberField(help_text='MOBILE FORMAT : +639178888888')
#
#     class Meta:
#         verbose_name_plural = 'Parents Information'
#
#     def __str__(self):
#         return '%s' % (self.mothersname, self.fathersname)


class Students(models.Model):
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='students', default="")
    studentname = models.CharField('Student Name', max_length=64)
    student_id = models.IntegerField('Student ID', blank=True, null=True)
    birthday = models.DateField('Date of Birth', default=date.today)
    lrn_no = models.CharField('Learners Number', default="", max_length=64, blank=True)
    profilepic = models.ImageField('Profile Picture',upload_to='profile_image', blank=True)
    groupinfo = models.ForeignKey('GradeGroup', on_delete=models.CASCADE, help_text="Choose appropriate Group")
    subjects = models.ManyToManyField('Subjects', help_text="Choose list of subjects")
    character = models.ManyToManyField('CharacterBuildingActivities', help_text="Choose list of Characters appropriated", verbose_name="Character Traits")

    class Meta:
        verbose_name_plural = 'LGMS Students Information'

    def __str__(self):
        return '%s' % (self.studentname)

class Faculty(models.Model):
    facultyname = models.CharField('Faculty Name', max_length=64)
    email = models.EmailField('Email Address', max_length=64,default='example@email.com')
    faculty_id = models.IntegerField('Faculty ID No.', default="1234")
    birthday = models.DateField('Date of Birth', default=date.today)

    groupinfo = {
        ('F', 'FACULTY'),
        ('S', 'STAFF'),
        ('SH', 'SCHOOL HEAD'),
    }

    rolegroup = models.CharField(max_length=10, choices=groupinfo, blank=True, default='F', help_text="Please choose Role / Duty")
    class Meta:
        verbose_name_plural = 'Teachers Info'

    def __str__(self):
        return '%s with CODE ID: %s' % (self.facultyname, self.email)

class GradeGroup(models.Model):
    gradename = models.CharField('Grade Year', blank=True, max_length=30)
    gradedesc = models.CharField('Grade Description', blank=True, max_length=64)

    class Meta:
        verbose_name_plural = 'LGMS Grade Year'

    def __str__(self):
        return '%s' % (self.gradename)


class Subjects(models.Model):
    subjectname = models.CharField('Subject Name', blank=False, max_length=64)
    color = models.CharField(max_length=64, default="#00b35c")

    class Meta:
        verbose_name_plural = 'Subjects Lists Information'


    def __str__(self):
       return '%s' % (self.subjectname)

    def get_html_badge(self):
        name = escape(self.subjectname)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, subjectname)
        return mark_safe(html)

    class Meta:
        verbose_name_plural = 'LGMS Subject Lists'

class CharacterBuildingActivities(models.Model):
    traitsname = models.CharField('Traits', max_length=64)

    def __str__(self):
        return '%s' % (self.traitsname)

    class Meta:
        verbose_name_plural = 'LGMS Character Lists'


class PresentCondition(models.Model):
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='presentcondition', default="")
    studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, default="")
    presentconditionchoices = {
        ('C', 'COLDS'),
        ('D', 'DIARRHEA'),
        ('L', 'LBM'),
        ('CO', 'COUGH'),
        ('F', 'FEVER'),
        ('H', 'HEADACHE'),
        ('S', 'STOMACH ACHE'),
        ('V', 'VOMITING'),
        ('0', 'OTHERS'),

    }
    currentcondition = models.CharField('Current Medical Condition', choices=presentconditionchoices, max_length=64)
    conditiondetails = models.TextField('Condition Details', max_length=64, blank=False)
    treatmentdetails = models.CharField('Treatment Information', max_length=64)
    startperiodofillness = models.DateField('Date Started', default=date.today)
    endperiodillness = models.DateField('Date Ended', default=date.today)

    def __str__(self):
        return '%s' % (self.studentname)

    def get_absolute_url(self):
        return reverse('studentbioid', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name_plural = 'Student Present Condition'




class IllnessInfo(models.Model):
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='illnessinfo', default="")
    studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, default="")
    illchoices = {
        ('A', 'Allergy'),
        ('ANE', 'Anemia'),
        ('AST', 'Asthma'),
        ('DP', 'Dermatology Problem'),
        ('DM', 'Diabetes Mellitus'),
        ('EP', 'Ear Problems'),
        ('GP', 'Gastrointestinal Problems'),
        ('HP', 'Heart Problem'),
        ('HMP', 'Hematologic Problem'),
        ('HT', 'Hypertension'),
        ('LP', 'Lung Problem'),
        ('MP', 'Metabolc Problem'),
        ('SZ', 'Seizures'),
        ('CV', 'Convulsion'),
        ('EPL', 'Epilepsy'),
        ('TP', 'Thyroid Problem'),
        ('VP', 'Viral Infection'),
        ('O', 'Others')

    }
    illnessinfo = models.CharField('Illness Information', choices=illchoices, default="A",max_length=64)
    illnessdetails = models.TextField('Details of Illness', max_length=300)
    treatmentdetails = models.CharField('Treatment Details', max_length=64, help_text="If under treatment, please indicate dosage of drug")
    startperiodofillness = models.DateField('Date Started', default=date.today)
    endperiodillness = models.DateField('Date Ended', default=date.today)

    def __str__(self):
        return '%s' % (self.name)

        #createview in views.py testing- this is related to somewhere
    # def get_absolute_url(self):
    #     return reverse('studentbioid', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name_plural = 'Student Illness Information'


class HospitalInfo(models.Model):
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='hospitalinfo', default="")
    studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, default="")
    reasonforhospital = models.CharField('Reason for Hospitalisation', max_length=64)
    hospitalisationdetails = models.TextField('Hospitalization Details', max_length=300)
    treatmentdetails = models.CharField('Treatment Details', max_length=64, help_text="If under treatment, please indicate dosage of drug")
    startperiodofillness = models.DateField('Date Started', default=date.today)
    endperiodillness = models.DateField('Date Ended', default=date.today)

    def __str__(self):
        return '%s' % (self.studentname)

        def get_absolute_url(self):
            return reverse('studentbioid', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name_plural = 'Student Hospital Info'


class AccidentInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=64, on_delete=models.CASCADE, blank=False, null=True, verbose_name=" Parents Name ")
    name = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE)
    accidentdetails = models.TextField('Accident Details', max_length=300)
    treatmentdetails = models.CharField('Treatment Details', max_length=64, help_text="If under treatment, please indicate dosage of drug")
    startperiodofillness = models.DateField('Date Started', default=date.today)
    endperiodillness = models.DateField('Date Ended', default=date.today)

    def __str__(self):
        return '%s' % (self.user)

        def get_absolute_url(self):
            return reverse('studentbioid', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name_plural = 'Student Accident Information'

class ImmunisationInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=64, on_delete=models.CASCADE, blank=False, null=True, verbose_name=" Parents Name ")
    name = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE)

    immunisationchoices = (

        ('NONE', 'NONE'),
        ('BCG', 'BCG'),
        ('DPT1', 'DPT1'),
        ('DPT2', 'DPT2'),
        ('DPT3', 'DPT3'),
        ('DPTB1', 'DPT Booster 1'),
        ('DPTB2', 'DPT Booster 2'),
        ('DPTB3', 'DPT Booster 3 range 13-19 years old'),
        ('POLIO 1','PLIO1'),
        ('POLIO2', 'PLIO2'),
        ('POLIO3', 'PLIO3'),
        ('POLIO BOOSTER 1', 'POLIO BOOSTER 1'),
        ('POLIO BOOSTER 2', 'POLIO BOOSTER 2'),
        ('HIB1', 'HIB 1'),
        ('HIB2', 'HIB 2'),
        ('HIB3', 'HIB 3'),
        ('HIB BOOSTER', 'HIB BOOSTER'),
        ('MEASLES', 'MEASLES'),
        ('MMR', 'MMR'),
        ('MMRB', 'MMRB'),
        ('HEPATITIS B1', 'HEPATITIS B1'),
        ('HEPATITIS B2', 'HEPATITIS B2'),
        ('HEPATITIS B3', 'HEPATITIS B3'),
        ('HEPATITIS B BOOSTER', 'HEPATITIS B BOOSTER'),
        ('HEPATITIS A1', 'HEPATITIS A1'),
        ('HEPATITIS A2', 'HEPATITIS A2'),
        ('VARICELLA - CHICKEN POX', 'VARICELLA - CHICKEN POX'),
        ('INFLUENZA', 'INFLUENZA'),
        ('TYPHOID', 'TYPHOID'),
    )
    immuneinfo = models.CharField('Immunisation Choices', choices=immunisationchoices, default="NONE",max_length=64)
    immunedetails = models.TextField('Immunisation Details', max_length=300, null=True, blank=True)
    treatmentdetails = models.CharField('Treatment Details', null=True, blank=True, max_length=64, help_text="If under treatment, please indicate dosage of drug")
    startperiodofimmune = models.DateField('Date Started', default=date.today)
    endperiodimmune = models.DateField('Date Ended', default=date.today)

    def __str__(self):
        return '%s : %s ' % (self.name, self.immuneinfo)

        def get_absolute_url(self):
            return reverse('studentbioid', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name_plural = 'Student Accident Immunisation Info'


#
# class StudentBio(models.Model):
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=64, on_delete=models.CASCADE, blank=False, null=True)
#     # username = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_username", on_delete=models.CASCADE, blank=True, null=True)
#     #username = models.OneToOneField('CustomUser', max_length=64, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Primary User Info")
#     studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE)
#     #parentsnameinfo = models.CharField('Parents Information', max_length=64, blank=True)
#     momsname = models.CharField('Mothers Name', max_length=64, blank=True)
#     popsname = models.CharField('Fathers Name', max_length=64, blank=True)
#     guardiansname = models.CharField('Guardians Name', max_length=64, blank=True)
#     gradeyear = models.ForeignKey('GradeYear', max_length=30, on_delete=models.CASCADE, related_name="gradeyear_gradeyear", verbose_name="Grade Year")
#     facultyname= models.ManyToManyField('Faculty', verbose_name="Faculty Assigned")
#     #we might omit this.
#     subjects = models.ManyToManyField('Subjects', verbose_name="List of Subjects", related_name="subjectslist")
#     charactersets = models.ManyToManyField('CharacterBuildingActivities', verbose_name="Character Sets")
#     profilepic = models.ImageField('Student Profile Picture',upload_to='profile_image', blank=True)
#     #test to connect to financial statement of account - still need to modify table starting from here..
#     financialinfo = models.ForeignKey('StatementAccount', verbose_name="Statement of Account", on_delete=models.CASCADE, max_length=64, blank=True, null=True)
#     profpicimage = models.ImageField('Student Profile Picture',upload_to='profile_image', blank=True)
#
#     class Meta:
#         verbose_name_plural = "Student Profile"
#
#     class Meta:
#         ordering = ['gradeyear']
#
#     def __str__(self):
#         return '%s : %s' % (self.id, self.studentname)
#
#


class StudentGrades(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=64, on_delete=models.CASCADE, blank=False, null=True)
    studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name")
    facultyname = models.ForeignKey('Faculty', default="", max_length=64, on_delete=models.CASCADE, verbose_name=" Teachers Name")
    subjectname = models.ForeignKey('Subjects', max_length=64, on_delete=models.CASCADE, verbose_name="Subject Name")

    grade = {
        ('76', 'B'),
        ('77-81','D'),
        ('82-86','AP'),
        ('87-91','P'),
        ('92-96','A'),
        ('97-100','E'),

    }
    grades = models.CharField('Grading System', choices=grade, default="B", max_length=64, help_text="Choose appropriate marks")

    dateperiod = models.DateField('Date Info Period', default=date.today)

    class Meta:
        verbose_name_plural = "Grades Records of Students"



class CharacterRatings(models.Model):
    studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name")
    charactersets = models.ForeignKey('CharacterBuildingActivities', max_length=64, on_delete=models.CASCADE, verbose_name=" Character Activities")
    guidelinesscore = {
        ('EXCELLENT', 'E'),
        ('VERY GOOD', 'VG'),
        ('GOOD', 'G'),
        ('FAIR / PASSED', 'F'),
        ('NEEDS IMPROVEMENT', 'NI'),
        ('UNSATISFACTORY / FAILED', 'U')
    }
    chargrades = models.CharField('Character Rates', choices=guidelinesscore, max_length=64, blank=False, default="EXCELLENT", help_text="Choose the appropriate grade")
    dateadded = models.DateField('Date Started', default=date.today)


    class Meta:
        verbose_name_plural = "Character Building Activities Records"


class ObservationLists(models.Model):
    traitsname = models.CharField('Traits', max_length=300)

    def __str__(self):
        return '%s' % (self.traitsname)

    class Meta:
        verbose_name_plural = "LGMS PAGUNLAD LISTS"

class CharacterObservation(models.Model):
    studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name")
    observationsets = models.ForeignKey('ObservationLists', max_length=64, on_delete=models.CASCADE, verbose_name=" Character Activities")
    observegrades = models.CharField('Character Rates', max_length=10, blank=False, default="G")
    dateadded = models.DateField('Date added', default=date.today)


    class Meta:
        verbose_name_plural = "LGMS PAGUNLAD SA TAGLAY NA MGA PAGPAPAHALAGA AT SALOOBIN LISTS"


# class TestRating(AbstractBaseRating):
#     #studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name")
#     foo = models.CharField(max_length=64)
#     #observationsets = models.ForeignKey('ObservationLists', max_length=64, on_delete=models.CASCADE, verbose_name=" Character Activities")


class StatementAccount(models.Model):
        studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name DB")
        gradeyear = models.ForeignKey('GradeGroup', max_length=30, on_delete=models.CASCADE, related_name="statement_gradegroup", verbose_name="Grade Year")
        term = {
            ('A', 'ANNUAL'),
            ('SA', 'SEMI-ANNUAL'),
            ('QRT', 'QUARTERLY'),
            ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'),
        }

        modeofpayment = models.CharField('Mode of Payment', choices=term, default="A", max_length=64, help_text="Choose Terms of Payment")
        modeofpaymenttotal = models.IntegerField('Mode Payment Total', default="1234")

        # def getterms(self):
        #     return self.modeofpayment + self.modeofpaymenttotal

        ### will try to edit from MoneyField to DecimalF or Integer###

        modeofpaymentprice = models.DecimalField('Mode of Payment Price', max_digits=20, decimal_places=4)
        ###this is where the money ###
        musicclassprice = models.DecimalField('Music Class Price', max_digits=20, decimal_places=4 )
        bookspricetotal = models.DecimalField('Books Price Total', max_digits=20, decimal_places=4)
        notebooks = models.DecimalField('Notebook Price', max_digits=20, decimal_places=4)
        uniforms = models.DecimalField('Uniform Price',max_digits=20, decimal_places=4)
        other = models.DecimalField('Miscellaneous & Others', max_digits=20, decimal_places=4)


        # def computetotal(self):
        #     return self.musicclassprice + self.bookspricetotal + self.notebooks + self.uniforms + self.other

        totalprice = models.IntegerField('Total Payment Price', default="1234")

        reservationfee = models.DecimalField('Reservation Fee', max_digits=20, decimal_places=4)
        discount = models.DecimalField('Discount Fee', max_digits=20, decimal_places=4)
        gtotal = models.IntegerField(default="0")



        # def gettotal(self):
        #     StatementAccount.objects.all().aggregate(Sum("Total Price", gtotal=IntegerField()))

        ### will try to edit from MoneyField to DecimalF or Integer end ###

        # modeofpaymentprice = MoneyField('Mode of Payment Price', max_digits=20, decimal_places=4, default_currency='PHP')
        # ###this is where the money ###
        # musicclassprice = MoneyField('Music Class Price', max_digits=20, decimal_places=4, default_currency='PHP')
        # bookspricetotal = MoneyField('Books Price Total', max_digits=20, decimal_places=4, default_currency='PHP')
        # notebooks = MoneyField('Notebook Price', max_digits=20, decimal_places=4, default_currency='PHP')
        # uniforms = MoneyField('Uniform Price',max_digits=20, decimal_places=4, default_currency='PHP')
        # other = MoneyField('Miscellaneous & Others', max_digits=20, decimal_places=4, default_currency='PHP')
        #
        # # def computetotal(self):
        # #     return self.musicclassprice + self.bookspricetotal + self.notebooks + self.uniforms + self.other
        #
        # totalprice = models.IntegerField('Total Payment Price', default="1234")
        #
        # reservationfee = MoneyField('Reservation Fee', max_digits=20, decimal_places=4, default_currency='PHP')
        # discount = MoneyField('Discount Fee', max_digits=20, decimal_places=4, default_currency='PHP')
        # gtotal = models.IntegerField('Grand Total Price', default="1234")

        # def calculate():


        def __str__(self):
            return '%s %s' % (self.studentname, self.gtotal)

        class Meta:
            verbose_name_plural = "Statement of Account"




class Compute(models.Model):
            studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name")
            testpayment1 = models.DecimalField('Mode of Payment', max_digits=20, decimal_places=2)
            testpayment2 = models.DecimalField('Mode of Payment Price', max_digits=20, decimal_places=2)
            # gtotal = property(gettotal)
            #
            #
            # @property
            # def gettotal(self):
            #     return '%s : %s' % self.testpayment1 * self.testpayment2


            class Meta:
                verbose_name_plural = "Computation Test Only"



class Document(models.Model):
    slug = models.SlugField()
    file = models.FileField(upload_to='object')

# class CharacterTagalogRatings(models.Model):
#     studentname = models.ForeignKey('Students', max_length=64, on_delete=models.CASCADE, verbose_name="Student Name"

# #sample rating
# class MyRating(AbstractBaseRating):
#    foo = models.TextField()

#testing of User profile



# class NewUsersList(models.Model):
#     newuserlist = users.*

#
# class Students(models.Model):
#     parents = models.OneToOneField('CustomUser', max_length=30, on_delete=models.CASCADE, related_name="parents_name")
#     childsname = models.ForeignKey('CustomUser', max_length=30, on_delete=models.CASCADE, related_name="childs_name")
#
#
#     def __str__(self):
#         return "%s %s" % (self.parents, self.childsname)
#
#     class Meta:
#         verbose_name_plural = 'Students Name and Info'
# #

#
# class Children(models.Model):
#     children = models.ForeignKey('Parents', max_length=30, on_delete=models.CASCADE, blank=True)
#
#     def __str__(self):
#         return '%s' % (self.children)
#
#     class Meta:
#         verbose_name_plural = 'Childrens Information'
#
#

#

#

#
#
#

#
# class AssessmentStudents(models.Model):
#     studentsname = models.CharField('Student Name', max_length=64)
#     status = models.CharField('Current Status of Student', max_length=64)
#     assessmentinfo = models.CharField('Assessment Info', max_length=64)
#
#     class Meta:
#         verbose_name_plural = 'Students Assessments Info'
#
#

# # class GuidelinesTraits():
# #     guidelinesscorechoices = {
# #         ('E', 'EXCELLENT'),
# #         ('VG', 'VERY GOOD'),
# #         ('G', 'GOOD'),
# #         ('F', 'FAIR or PASSED'),
# #         ('NI', 'NEEDS IMPROVEMENT'),
# #         ('U', 'UNSATISFACTORY'),
# #     }
# #
# #     guidelinesscore = models.CharField(max_length=30, choices=guidelinesscorechoices, blank=True, default='E', help_text="Please select Guidelines Score")
# #
# #
#
#
#         #later I will try to add data then connect students to Users so that I can show it to the profile
#


#this is for extending user



# Create your models here.


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, name, date_of_birth, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email = self.normalize_email(email),
#             name = name,
#             date_of_birth=date_of_birth,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, name, date_of_birth, password):
#
#         user =
