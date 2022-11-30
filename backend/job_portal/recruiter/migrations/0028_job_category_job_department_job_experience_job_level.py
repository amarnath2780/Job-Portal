# Generated by Django 4.1.3 on 2022-11-29 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0003_alter_companycategory_category_name'),
        ('recruiter', '0027_rename_company_job_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.companycategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.companydepartment'),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='level',
            field=models.CharField(blank=True, choices=[('fresher', 'Fresher'), ('intermediate', 'Intermediate'), ('professional', 'Professional')], default='fresher', max_length=200),
        ),
    ]