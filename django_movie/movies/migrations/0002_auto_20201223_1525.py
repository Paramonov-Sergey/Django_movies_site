# Generated by Django 3.1.2 on 2020-12-23 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'Пол', 'verbose_name_plural': 'Пол'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
