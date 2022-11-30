# Generated by Django 4.1.3 on 2022-11-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0003_alter_companycategory_category_name'),
        ('seeker', '0020_alter_appliedjob_recruiter_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seekerprofile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.companydepartment'),
        ),
        migrations.AddField(
            model_name='seekerprofile',
            name='level',
            field=models.CharField(blank=True, choices=[('fresher', 'Fresher'), ('intermediate', 'Intermediate'), ('professional', 'Professional')], default='fresher', max_length=200),
        ),
    ]
