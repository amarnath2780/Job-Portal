# Generated by Django 4.1.3 on 2022-11-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0003_alter_companycategory_category_name'),
        ('recruiter', '0022_rename_profile_pic_recruiterprofile_profie_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiterprofile',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.companycategory'),
        ),
    ]
