# Generated by Django 4.1.3 on 2022-11-29 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0028_job_category_job_department_job_experience_job_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='posted_at',
            new_name='created_at',
        ),
    ]