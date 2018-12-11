# Generated by Django 2.1.2 on 2018-12-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0149_auto_20181205_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('GOOD', 'G'), ('FAIR / PASSED', 'F'), ('NEEDS IMPROVEMENT', 'NI'), ('UNSATISFACTORY / FAILED', 'U'), ('VERY GOOD', 'VG'), ('EXCELLENT', 'E')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('D', 'Divorcee'), ('M', 'Married'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Catholic'), ('M', 'Muslim'), ('B', 'Buddhist'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('S', 'STAFF'), ('SH', 'SCHOOL HEAD')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('EP', 'Ear Problems'), ('EPL', 'Epilepsy'), ('HT', 'Hypertension'), ('O', 'Others'), ('HMP', 'Hematologic Problem'), ('TP', 'Thyroid Problem'), ('VP', 'Viral Infection'), ('ANE', 'Anemia'), ('SZ', 'Seizures'), ('HP', 'Heart Problem'), ('GP', 'Gastrointestinal Problems'), ('DP', 'Dermatology Problem'), ('AST', 'Asthma'), ('MP', 'Metabolc Problem'), ('CV', 'Convulsion'), ('A', 'Allergy'), ('LP', 'Lung Problem'), ('DM', 'Diabetes Mellitus')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('C', 'COLDS'), ('F', 'FEVER'), ('CO', 'COUGH'), ('D', 'DIARRHEA'), ('H', 'HEADACHE'), ('V', 'VOMITING'), ('0', 'OTHERS'), ('L', 'LBM'), ('S', 'STOMACH ACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('SA', 'SEMI-ANNUAL'), ('A', 'ANNUAL'), ('QRT', 'QUARTERLY')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('82-86', 'AP'), ('87-91', 'P'), ('92-96', 'A'), ('97-100', 'E'), ('77-81', 'D')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
    ]
