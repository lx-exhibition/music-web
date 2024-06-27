# Generated by Django 5.0.3 on 2024-03-28 01:28

import django.db.models.deletion
import utils.coder
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='artist',
            name='background',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='background_artists', to='music.image'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(blank=True, db_default='这家伙什么都没留下...', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='data',
            field=models.ImageField(upload_to=utils.coder.encode_upload_image),
        ),
        migrations.AlterField(
            model_name='song',
            name='data',
            field=models.FileField(upload_to=utils.coder.encode_upload_video),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='music.image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fans',
            field=models.ManyToManyField(blank=True, null=True, related_name='concerns', to='music.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.location'),
        ),
        migrations.AlterField(
            model_name='user',
            name='msg_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='msged_users', through='music.Message', to='music.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(db_default='用户已注销', max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='data',
            field=models.FileField(upload_to=utils.coder.encode_upload_video),
        ),
    ]
