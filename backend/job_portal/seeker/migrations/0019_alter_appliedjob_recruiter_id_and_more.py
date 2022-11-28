# Generated by Django 4.1.3 on 2022-11-28 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0027_rename_company_job_company_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seeker', '0018_alter_appliedjob_recruiter_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedjob',
            name='recruiter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.recruiterprofile'),
        ),
        migrations.AlterField(
            model_name='appliedjob',
            name='seeker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
