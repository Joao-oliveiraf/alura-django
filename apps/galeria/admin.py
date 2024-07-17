from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "data_fotografia", "publicada", "usuario")
    list_display_links = ("id", "nome")
    list_editable = ("publicada",)
    search_fields = ("nome", "legenda")
    list_filter = ("categoria", "usuario")
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
