# Generated by Django 5.0.3 on 2024-04-04 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_a_test_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a_test',
            name='img',
        ),
    ]