# Generated by Django 3.2.9 on 2022-01-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsApp', '0003_auto_20220109_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(max_length=400, verbose_name='Tu consulta'),
        ),
    ]