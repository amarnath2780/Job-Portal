# Generated by Django 4.1.3 on 2022-12-06 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0025_rename_shortlisted_appliedjob_is_shortlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjob',
            name='is_decline',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
