# Generated by Django 4.1.3 on 2022-12-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_remove_shorlistedappliedseekers_recruiter_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorlistedappliedseekers',
            name='send',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
