# Generated by Django 2.2.4 on 2019-08-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20190810_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_model',
            field=models.BooleanField(default=False, verbose_name='모델'),
        ),
    ]