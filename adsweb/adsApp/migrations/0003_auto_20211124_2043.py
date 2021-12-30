# Generated by Django 3.2.9 on 2021-11-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsApp', '0002_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('file', models.FileField(default='null', upload_to='')),
                ('description', models.TextField(max_length=400)),
                ('suscription', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['created_at'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='images', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='article',
            name='public',
            field=models.BooleanField(verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado'),
        ),
        migrations.AlterField(
            model_name='section',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creada'),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.CharField(max_length=400, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Sección'),
        ),
    ]