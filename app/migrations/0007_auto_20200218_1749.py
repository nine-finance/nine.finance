# Generated by Django 2.2.9 on 2020-02-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200216_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_media'),
        ),
    ]
