from django.contrib import admin
from .models import Projeto

# Register your models here.


class ListandoProjetos(admin.ModelAdmin):
    """
    Classe para modificar a listagem de projetos no admin.
    """
    list_filter = ('cliente', )
    list_display = ('id', 'nome_projeto', 'data_conclusao')
    list_display_links = ('id', 'nome_projeto', 'data_conclusao')
    search_fields = ('nome_projeto', )


admin.site.register(Projeto, ListandoProjetos)
