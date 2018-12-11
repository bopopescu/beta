# Generated by Django 2.1.2 on 2018-12-05 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0144_auto_20181205_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illnessinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='illnessinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='presentcondition',
            name='name',
        ),
        migrations.RemoveField(
            model_name='presentcondition',
            name='user',
        ),
        migrations.AddField(
            model_name='illnessinfo',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='illnessinfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='presentcondition',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='presentcondition', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('EXCELLENT', 'E'), ('UNSATISFACTORY / FAILED', 'U'), ('NEEDS IMPROVEMENT', 'NI'), ('GOOD', 'G'), ('FAIR / PASSED', 'F'), ('VERY GOOD', 'VG')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('SP', 'Single Parent'), ('W', 'Widowed'), ('M', 'Married')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('I', 'INC'), ('B', 'Buddhist'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('S', 'STAFF'), ('SH', 'SCHOOL HEAD'), ('F', 'FACULTY')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('HMP', 'Hematologic Problem'), ('A', 'Allergy'), ('HT', 'Hypertension'), ('LP', 'Lung Problem'), ('MP', 'Metabolc Problem'), ('TP', 'Thyroid Problem'), ('ANE', 'Anemia'), ('VP', 'Viral Infection'), ('DP', 'Dermatology Problem'), ('AST', 'Asthma'), ('EP', 'Ear Problems'), ('CV', 'Convulsion'), ('DM', 'Diabetes Mellitus'), ('GP', 'Gastrointestinal Problems'), ('O', 'Others'), ('HP', 'Heart Problem'), ('EPL', 'Epilepsy'), ('SZ', 'Seizures')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('CO', 'COUGH'), ('L', 'LBM'), ('H', 'HEADACHE'), ('D', 'DIARRHEA'), ('F', 'FEVER'), ('0', 'OTHERS'), ('V', 'VOMITING'), ('C', 'COLDS'), ('S', 'STOMACH ACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('A', 'ANNUAL'), ('QRT', 'QUARTERLY'), ('SA', 'SEMI-ANNUAL'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('77-81', 'D'), ('92-96', 'A'), ('87-91', 'P'), ('82-86', 'AP'), ('76', 'B'), ('97-100', 'E')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
    ]
