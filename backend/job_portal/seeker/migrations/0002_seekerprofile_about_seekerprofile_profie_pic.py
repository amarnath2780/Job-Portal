# Generated by Django 4.1.3 on 2022-11-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seekerprofile',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='seekerprofile',
            name='profie_pic',
            field=models.ImageField(blank=True, upload_to='', verbose_name='/images/'),
        ),
    ]