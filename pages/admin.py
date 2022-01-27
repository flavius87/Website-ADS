from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article
class PageResource(resources.ModelResource):

    class Meta: 
        model = Page
class AssideResource(resources.ModelResource):

    class Meta:
        model = Asside
class VideoResource(resources.ModelResource):

    class Meta:
        model = Video
class GalleryImagesResource(resources.ModelResource):
    class Meta:
        model = GalleryImages          
class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery  



class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'public')
    resource_class = ArticleResource

class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'visible')
    resource_class = PageResource

class AssideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at')
    resources_class = AssideResource

class VideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'caption')
    resources_class = VideoResource

class GalleryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    resource_class = GalleryResource
    class Meta:
        model=Gallery

class GalleryImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    resource_class = GalleryImagesResource


# Registros

admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Asside, AssideAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImages, GalleryImagesAdmin)


# Configurar el título del panel
title = "ADS - Construcción en seco"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle


