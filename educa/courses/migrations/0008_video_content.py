# Generated by Django 2.2 on 2019-04-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190416_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='content',
            field=models.TextField(default=0),
        ),
    ]