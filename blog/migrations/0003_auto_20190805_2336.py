# Generated by Django 2.2.4 on 2019-08-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190805_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_writer',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
