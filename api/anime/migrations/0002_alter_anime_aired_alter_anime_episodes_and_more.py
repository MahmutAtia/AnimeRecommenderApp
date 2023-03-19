# Generated by Django 4.1.7 on 2023-03-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='aired',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='anime',
            name='img_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='anime',
            name='ranked',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='anime',
            name='score',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='anime',
            name='synopsis',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.CharField(default='', max_length=128),
        ),
    ]