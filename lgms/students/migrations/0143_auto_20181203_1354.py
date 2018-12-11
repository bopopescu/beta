# Generated by Django 2.1.2 on 2018-12-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0142_auto_20181203_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('EXCELLENT', 'E'), ('FAIR / PASSED', 'F'), ('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U'), ('GOOD', 'G'), ('NEEDS IMPROVEMENT', 'NI')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('W', 'Widowed'), ('SP', 'Single Parent'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('M', 'Muslim'), ('I', 'INC'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('GP', 'Gastrointestinal Problems'), ('EPL', 'Epilepsy'), ('CV', 'Convulsion'), ('A', 'Allergy'), ('DM', 'Diabetes Mellitus'), ('EP', 'Ear Problems'), ('AST', 'Asthma'), ('TP', 'Thyroid Problem'), ('VP', 'Viral Infection'), ('LP', 'Lung Problem'), ('O', 'Others'), ('MP', 'Metabolc Problem'), ('DP', 'Dermatology Problem'), ('HT', 'Hypertension'), ('HP', 'Heart Problem'), ('ANE', 'Anemia'), ('SZ', 'Seizures'), ('HMP', 'Hematologic Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('L', 'LBM'), ('H', 'HEADACHE'), ('V', 'VOMITING'), ('D', 'DIARRHEA'), ('C', 'COLDS'), ('CO', 'COUGH'), ('F', 'FEVER'), ('S', 'STOMACH ACHE'), ('0', 'OTHERS')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('SA', 'SEMI-ANNUAL'), ('A', 'ANNUAL'), ('QRT', 'QUARTERLY'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('82-86', 'AP'), ('87-91', 'P'), ('92-96', 'A'), ('77-81', 'D'), ('97-100', 'E')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
    ]
