from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class SliderResource(resources.ModelResource):
    class Meta:
        model = Slider

class SliderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'order',)
    resource_class = SliderResource

# Register your models here.
admin.site.register(Contact)
admin.site.register(Slider, SliderAdmin)

# Configurar el título del panel
title = "ADS - Construcción en seco"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestión"