# Generated by Django 2.2.4 on 2019-08-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_remove_user_buleanito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='is_model',
            field=models.NullBooleanField(default=True, verbose_name='모델'),
        ),
    ]
