# Generated by Django 5.1.4 on 2025-02-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_bookmarksfolders_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='reels',
            name='shares',
            field=models.IntegerField(default=0, verbose_name='Кол-во репостов'),
        ),
        migrations.AddField(
            model_name='reels',
            name='tags',
            field=models.TextField(default=' ', verbose_name='Тэги рилса'),
        ),
    ]
