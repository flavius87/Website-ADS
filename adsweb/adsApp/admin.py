from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Slider)

# Configurar el título del panel
title = "ADS - Construcción en seco"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestión"