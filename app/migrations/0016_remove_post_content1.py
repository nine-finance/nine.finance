# Generated by Django 2.2.9 on 2020-04-07 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_post_content1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content1',
        ),
    ]
