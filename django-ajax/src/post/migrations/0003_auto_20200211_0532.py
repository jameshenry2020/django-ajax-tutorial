# Generated by Django 3.0.3 on 2020-02-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_like_likecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likecount',
        ),
        migrations.AddField(
            model_name='article',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
    ]