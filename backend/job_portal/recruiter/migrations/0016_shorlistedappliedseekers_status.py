# Generated by Django 4.1.3 on 2022-12-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiter", "0015_alter_job_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="shorlistedappliedseekers",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Shortlised", "Shortlised"),
                    ("Tech-Interview", "Tech-Interview"),
                    ("HR-Round", "HR-Round"),
                ],
                default="Shortlised",
                max_length=200,
            ),
        ),
    ]
