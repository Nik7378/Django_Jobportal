# Generated by Django 4.1.5 on 2023-03-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_job_experience_alter_job_job_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='vacancies',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='yop',
            field=models.CharField(max_length=4),
        ),
    ]
