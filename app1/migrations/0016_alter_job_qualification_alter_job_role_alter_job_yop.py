# Generated by Django 4.1.5 on 2023-03-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_job_venue_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='qualification',
            field=models.CharField(choices=[('Any Degree', 'Any Degree'), ('M.E/M.Tech/M.S', 'M.E/M.Tech/M.S'), ('B.E/B.Tech', 'B.E/B.Tech'), ('MBA', 'MBA'), ('Diploma', 'Diploma')], max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='role',
            field=models.CharField(choices=[('Select job role', 'Select job role'), ('App developer', 'App developer'), ('Database administrator', 'Database administrator'), ('Service desk analyst', 'Service desk analyst'), ('Software developer', 'Software developer'), ('Software engineer', 'Software engineer'), ('Software tester', 'Software tester'), ('Web developer', 'Web developer')], default='Select job role', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='yop',
            field=models.CharField(max_length=50),
        ),
    ]
