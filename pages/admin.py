from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article

class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'public')
    resource_class = ArticleResource

admin.site.register(Article, ArticleAdmin)

class PageResource(resources.ModelResource):

    class Meta: 
        model = Page

class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'visible')
    resource_class = PageResource

admin.site.register(Page, PageAdmin)

class AssideResource(resources.ModelResource):

    class Meta:
        model = Asside
class AssideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at')
    resources_class = AssideResource

admin.site.register(Asside, AssideAdmin)

class VideoResource(resources.ModelResource):

    class Meta:
        model = Video

class VideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'caption')
    resources_class = VideoResource

admin.site.register(Video, VideoAdmin)

# Gallery


class GalleryImagesAdmin(admin.StackedInline):
    model=GalleryImages

class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery  

class GalleryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [GalleryImagesAdmin]
    resource_class = GalleryResource
admin.site.register(Gallery, GalleryAdmin)

class GalleryImagesResource(resources.ModelResource):
    class Meta:
        model = GalleryImages  
class GalleryImagesAdmin(admin.ModelAdmin):
    pass
    resource_class = GalleryImagesResource
admin.site.register(GalleryImages, GalleryImagesAdmin)

# Configurar el título del panel
title = "ADS - Construcción en seco"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
