# Generated by Django 3.2.9 on 2021-11-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsApp', '0006_alter_contact_suscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='file',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='suscription',
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.TextField(max_length=100),
        ),
    ]
