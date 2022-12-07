# Generated by Django 4.1.3 on 2022-12-07 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificaiton',
            name='receive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_revoker', to='recruiter.recruiterprofile'),
        ),
        migrations.AddField(
            model_name='notificaiton',
            name='status',
            field=models.CharField(blank=True, default='unread', max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='notificaiton',
            name='type_of_notification',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='notificaiton',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='seeker.seekerprofile'),
        ),
    ]
