# Generated by Django 4.1.5 on 2023-03-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_job_experience_alter_job_job_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='yop',
            field=models.DateField(),
        ),
    ]
