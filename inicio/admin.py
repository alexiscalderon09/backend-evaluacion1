from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "url", "creado")
    search_fields = ("nombre",)
