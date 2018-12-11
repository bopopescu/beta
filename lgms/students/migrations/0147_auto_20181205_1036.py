# Generated by Django 2.1.2 on 2018-12-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0146_auto_20181205_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('NEEDS IMPROVEMENT', 'NI'), ('VERY GOOD', 'VG'), ('EXCELLENT', 'E'), ('UNSATISFACTORY / FAILED', 'U'), ('GOOD', 'G'), ('FAIR / PASSED', 'F')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('D', 'Divorcee'), ('M', 'Married'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('C', 'Catholic'), ('I', 'INC'), ('B', 'Buddhist')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('S', 'STAFF'), ('F', 'FACULTY')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('ANE', 'Anemia'), ('HP', 'Heart Problem'), ('HT', 'Hypertension'), ('MP', 'Metabolc Problem'), ('VP', 'Viral Infection'), ('O', 'Others'), ('CV', 'Convulsion'), ('AST', 'Asthma'), ('SZ', 'Seizures'), ('TP', 'Thyroid Problem'), ('EP', 'Ear Problems'), ('DM', 'Diabetes Mellitus'), ('HMP', 'Hematologic Problem'), ('LP', 'Lung Problem'), ('A', 'Allergy'), ('EPL', 'Epilepsy'), ('GP', 'Gastrointestinal Problems'), ('DP', 'Dermatology Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('L', 'LBM'), ('F', 'FEVER'), ('V', 'VOMITING'), ('CO', 'COUGH'), ('D', 'DIARRHEA'), ('H', 'HEADACHE'), ('C', 'COLDS'), ('0', 'OTHERS'), ('S', 'STOMACH ACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('A', 'ANNUAL'), ('SA', 'SEMI-ANNUAL'), ('QRT', 'QUARTERLY'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('97-100', 'E'), ('82-86', 'AP'), ('87-91', 'P'), ('76', 'B'), ('92-96', 'A'), ('77-81', 'D')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='lrn_no',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Learners Number'),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.IntegerField(blank=True, verbose_name='Student ID'),
        ),
    ]
