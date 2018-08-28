# Generated by Django 2.0.6 on 2018-08-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0113_auto_20180827_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentbio',
            name='profpicimage',
            field=models.ImageField(blank=True, upload_to='profile_image', verbose_name='Student Profile Picture'),
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('VERY GOOD', 'VG'), ('GOOD', 'G'), ('FAIR / PASSED', 'F'), ('NEEDS IMPROVEMENT', 'NI'), ('EXCELLENT', 'E'), ('UNSATISFACTORY / FAILED', 'U')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('SPED', 'Special Education Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('M', 'Married'), ('SP', 'Single Parent'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('C', 'Catholic'), ('I', 'INC'), ('M', 'Muslim')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('VP', 'Viral Infection'), ('AST', 'Asthma'), ('SZ', 'Seizures'), ('MP', 'Metabolc Problem'), ('CV', 'Convulsion'), ('A', 'Allergy'), ('DP', 'Dermatology Problem'), ('EP', 'Ear Problems'), ('LP', 'Lung Problem'), ('HMP', 'Hematologic Problem'), ('DM', 'Diabetes Mellitus'), ('EPL', 'Epilepsy'), ('GP', 'Gastrointestinal Problems'), ('TP', 'Thyroid Problem'), ('ANE', 'Anemia'), ('O', 'Others'), ('HT', 'Hypertension'), ('HP', 'Heart Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('C', 'COLDS'), ('H', 'HEADACHE'), ('D', 'DIARRHEA'), ('L', 'LBM'), ('CO', 'COUGH'), ('V', 'VOMITING'), ('S', 'STOMACH ACHE'), ('0', 'OTHERS'), ('F', 'FEVER')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('QRT', 'QUARTERLY'), ('SA', 'SEMI-ANNUAL'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('A', 'ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('92-96', 'A'), ('76', 'B'), ('97-100', 'E'), ('87-91', 'P'), ('77-81', 'D'), ('82-86', 'AP')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE 2', 'G2'), ('GRADE 1', 'G1'), ('GRADE 6', 'G6'), ('PLAY GROUP', 'PG'), ('CASA AFTERNOON 1:30', 'CA'), ('GRADE 10', 'G10'), ('GRADE 8', 'G8'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('GRADE 5', 'G5'), ('TEACH PM', 'TEP'), ('GRADE 9', 'G9'), ('GRADE 7', 'G7'), ('TEACH AM', 'TEA'), ('GRADE 3', 'G3'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('GRADE 4', 'G4'), ('CASA AM', 'CM')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('S', 'STAFF'), ('SH', 'SCHOOL HEAD'), ('F', 'FACULTY')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]