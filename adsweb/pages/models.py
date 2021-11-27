from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=60, verbose_name="Título")
    content = RichTextField(default='null', verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='images')
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    order = models.IntegerField(default=0, verbose_name="Orden de página")
    dropdown_one = models.BooleanField(default=False, verbose_name="Menú desplegable uno")
    dropdown_two = models.BooleanField(default=False, verbose_name="Menú desplegable dos")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title

