# Generated by Django 4.1.3 on 2022-12-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0007_remove_recruiterprofile_plan_expires_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.membershipspurchaces'),
        ),
    ]
