from django.contrib import admin
from galeria import models
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "data_fotografia", "publicada")
    list_display_links = ("id", "nome")
    list_editable = ("publicada",)
    search_fields = ("nome", "legenda")
    list_filter = ("categoria",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
