# Generated by Django 3.1.2 on 2020-12-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20201224_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='devorced',
            field=models.ManyToManyField(blank=True, null=True, related_name='_actor_devorced_+', to='movies.Actor'),
        ),
    ]
