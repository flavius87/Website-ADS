from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Page)

# Configurar el título del panel
title = "ADS - Construcción en seco"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle