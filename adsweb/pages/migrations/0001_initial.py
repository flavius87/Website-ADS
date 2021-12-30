# Generated by Django 3.2.9 on 2021-11-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(default='null', upload_to='images', verbose_name='Imagen')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL amigable')),
                ('visible', models.BooleanField(verbose_name='¿Visible?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
            },
        ),
    ]