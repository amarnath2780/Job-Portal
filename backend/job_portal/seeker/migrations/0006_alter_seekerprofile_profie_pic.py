# Generated by Django 4.1.3 on 2022-11-25 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0005_profilepic_alter_seekerprofile_profie_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofile',
            name='profie_pic',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seeker.profilepic'),
        ),
    ]