# Generated by Django 3.1.2 on 2020-12-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_qualityvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='quality_videos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.qualityvideos', verbose_name='Качество видео'),
        ),
    ]
