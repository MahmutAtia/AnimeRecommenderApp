# Generated by Django 4.1.7 on 2023-03-21 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_alter_anime_aired_alter_anime_episodes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ['-score']},
        ),
    ]
