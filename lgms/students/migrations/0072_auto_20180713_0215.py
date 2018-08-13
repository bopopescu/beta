# Generated by Django 2.0.6 on 2018-07-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0071_auto_20180713_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JH', 'Junior High School Program'), ('SH', 'Senior High School Program'), ('CA', 'CASA Program'), ('SPED', 'Special Education Program'), ('GS', 'Grade School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('D', 'Divorcee'), ('SP', 'Single Parent'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('M', 'Muslim'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('AST', 'Asthma'), ('HMP', 'Hematologic Problem'), ('LP', 'Lung Problem'), ('HT', 'Hypertension'), ('GP', 'Gastrointestinal Problems'), ('A', 'Allergy'), ('SZ', 'Seizures'), ('CV', 'Convulsion'), ('DP', 'Dermatology Problem'), ('MP', 'Metabolc Problem'), ('EPL', 'Epilepsy'), ('ANE', 'Anemia'), ('VP', 'Viral Infection'), ('EP', 'Ear Problems'), ('DM', 'Diabetes Mellitus'), ('O', 'Others'), ('HP', 'Heart Problem'), ('TP', 'Thyroid Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('0', 'OTHERS'), ('S', 'STOMACH ACHE'), ('D', 'DIARRHEA'), ('H', 'HEADACHE'), ('V', 'VOMITING'), ('L', 'LBM'), ('F', 'FEVER'), ('C', 'COLDS'), ('CO', 'COUGH')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('G1', 'GRADE 1'), ('G7', 'GRADE 7'), ('G8', 'GRADE 8'), ('G10', 'GRADE 10'), ('G2', 'GRADE 2'), ('G6', 'GRADE 6'), ('CA', 'CASA AFTERNOON 1:30'), ('TEP', 'TEACH PM'), ('G4', 'GRADE 4'), ('G9', 'GRADE 9'), ('PG', 'PLAY GROUP'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('TEA', 'TEACH AM'), ('G5', 'GRADE 5'), ('CM', 'CASA AM'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('G3', 'GRADE 3')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('S', 'STAFF'), ('SH', 'SCHOOL HEAD')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.AlterField(
            model_name='testrating',
            name='foo',
            field=models.CharField(max_length=64),
        ),
    ]