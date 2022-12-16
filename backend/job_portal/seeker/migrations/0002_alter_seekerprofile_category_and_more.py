# Generated by Django 4.1.3 on 2022-12-16 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0004_banner'),
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofile',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.companycategory'),
        ),
        migrations.AlterField(
            model_name='seekerprofile',
            name='department',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.companydepartment'),
        ),
        migrations.AlterField(
            model_name='seekerprofile',
            name='experince',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
