from django.contrib import admin
from roupas.models import *

class ListandoConjuntos(admin.ModelAdmin):
    list_display = ('id', 'nome_conjunto', 'preco_conjunto', 'categoria_conjunto', 'get_date_formated', 'status_conjunto' )
    list_display_links = ('id','nome_conjunto')
    search_fields = ('nome_conjunto',)
    list_filter = ('categoria_conjunto','data_conjunto', 'status_conjunto')
    list_editable = ('status_conjunto',)

    def get_date_formated(self, obj):
        if obj.data_conjunto:
            return obj.data_conjunto.strftime('%d/%m/%Y')
    
    get_date_formated.short_description = 'data de publicação'

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'preco_produto', 'categoria_produto', 'get_date_formated', 'status_produto' )
    list_display_links = ('id','nome_produto')
    search_fields = ('nome_produto',)
    list_filter = ('categoria_produto','data_produto', 'status_produto')
    list_editable = ('status_produto',)

    def get_date_formated(self, obj):
        if obj.data_produto:
            return obj.data_produto.strftime('%d/%m/%Y')
    
    get_date_formated.short_description = 'data de publicação'


admin.site.register(ConjuntoRoupas, ListandoConjuntos)
admin.site.register(Produto, ListandoProdutos)
