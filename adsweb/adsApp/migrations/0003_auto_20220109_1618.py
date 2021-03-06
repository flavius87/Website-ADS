# Generated by Django 3.2.9 on 2022-01-09 19:18

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('adsApp', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.TextField(max_length=150, validators=[django.core.validators.RegexValidator('^[A-Za-z-ñ ]*$', 'El campo ciudad no puede contener números o caracteres especiales')], verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(max_length=400, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-Za-z-ñ ]*$', 'El asunto no puede contener números o caracteres especiales')], verbose_name='Asunto'),
        ),
    ]
