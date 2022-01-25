from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Page)
admin.site.register(Asside)
admin.site.register(Video)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'public')

admin.site.register(Article, ArticleAdmin)


# Gallery
class GalleryImagesAdmin(admin.StackedInline):
    model=GalleryImages

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImagesAdmin]

    class Meta:
        model=Gallery

@admin.register(GalleryImages)
class GalleryImagesAdmin(admin.ModelAdmin):
    pass

# Configurar el título del panel
title = "ADS - Construcción en seco"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
