# Generated by Django 3.2.9 on 2021-12-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='URL amigable'),
        ),
    ]
