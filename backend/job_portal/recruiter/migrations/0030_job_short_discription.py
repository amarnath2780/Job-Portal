# Generated by Django 4.1.3 on 2022-11-30 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0029_rename_posted_at_job_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='short_discription',
            field=models.TextField(blank=True),
        ),
    ]
