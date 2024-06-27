# Generated by Django 5.0.3 on 2024-04-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fans',
            field=models.ManyToManyField(blank=True, related_name='concerns', to='music.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='msg_users',
            field=models.ManyToManyField(blank=True, related_name='msged_users', through='music.Message', to='music.user'),
        ),
    ]
