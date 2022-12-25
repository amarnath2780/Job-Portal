# Generated by Django 4.1.3 on 2022-12-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seeker", "0002_alter_seekerprofile_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appliedjob",
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
