# Generated by Django 3.1.2 on 2020-12-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_movie_treiler'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='english_title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название на английском'),
        ),
    ]
