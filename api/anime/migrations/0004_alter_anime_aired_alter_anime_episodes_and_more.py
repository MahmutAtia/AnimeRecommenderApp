# Generated by Django 4.1.7 on 2023-03-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_alter_anime_episodes_alter_anime_img_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='aired',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.FloatField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, to='anime.genre'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='img_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='ranked',
            field=models.FloatField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='score',
            field=models.FloatField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='synopsis',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
    ]
