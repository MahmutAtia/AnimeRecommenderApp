# Generated by Django 4.1.7 on 2023-03-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('synopsis', models.TextField()),
                ('img_url', models.URLField()),
                ('aired', models.CharField(max_length=128)),
                ('episodes', models.FloatField()),
                ('ranked', models.FloatField()),
                ('score', models.FloatField()),
                ('genre', models.ManyToManyField(to='anime.genre')),
            ],
        ),
    ]
