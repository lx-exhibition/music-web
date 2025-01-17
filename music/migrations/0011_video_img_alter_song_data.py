# Generated by Django 5.0.3 on 2024-04-15 14:26

import django.db.models.deletion
import utils.coder
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_alter_user_fans_alter_user_msg_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='img',
            field=models.ForeignKey(default=282, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='music.image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='data',
            field=models.FileField(upload_to=utils.coder.encode_upload_music),
        ),
    ]
