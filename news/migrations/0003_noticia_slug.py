# Generated by Django 3.1 on 2021-06-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210601_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(default='DEFAULT VALUE SLUG', max_length=200, unique=True),
        ),
    ]
