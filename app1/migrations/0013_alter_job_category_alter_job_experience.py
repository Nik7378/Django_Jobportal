# Generated by Django 4.1.5 on 2023-03-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_job_category_alter_job_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('entry level', 'Entry-Level'), ('mid level', 'Mid-Level'), ('senior level', 'Senior-Level')], max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('3+', '3+')], max_length=2),
        ),
    ]
