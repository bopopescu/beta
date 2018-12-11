# Generated by Django 2.1.2 on 2018-12-03 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0141_auto_20181203_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('EXCELLENT', 'E'), ('VERY GOOD', 'VG'), ('GOOD', 'G'), ('NEEDS IMPROVEMENT', 'NI'), ('FAIR / PASSED', 'F'), ('UNSATISFACTORY / FAILED', 'U')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('M', 'Married'), ('D', 'Divorcee'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('I', 'INC'), ('M', 'Muslim'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('HP', 'Heart Problem'), ('CV', 'Convulsion'), ('A', 'Allergy'), ('HMP', 'Hematologic Problem'), ('EPL', 'Epilepsy'), ('EP', 'Ear Problems'), ('MP', 'Metabolc Problem'), ('DM', 'Diabetes Mellitus'), ('TP', 'Thyroid Problem'), ('LP', 'Lung Problem'), ('VP', 'Viral Infection'), ('O', 'Others'), ('AST', 'Asthma'), ('GP', 'Gastrointestinal Problems'), ('HT', 'Hypertension'), ('ANE', 'Anemia'), ('DP', 'Dermatology Problem'), ('SZ', 'Seizures')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('V', 'VOMITING'), ('F', 'FEVER'), ('CO', 'COUGH'), ('L', 'LBM'), ('H', 'HEADACHE'), ('D', 'DIARRHEA'), ('C', 'COLDS'), ('S', 'STOMACH ACHE'), ('0', 'OTHERS')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('SA', 'SEMI-ANNUAL'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('QRT', 'QUARTERLY'), ('A', 'ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('87-91', 'P'), ('76', 'B'), ('92-96', 'A'), ('77-81', 'D'), ('82-86', 'AP'), ('97-100', 'E')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
    ]
