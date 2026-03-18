from django.contrib import admin

from .models import Produto, Cliente, Perfil, Venda, itemVenda


@admin .register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'qtde', 'descricao','data','imagem')
    list_display_links = ('nome', ' ')
    search_fields = ('nome', 'qtde')
    list_editable = ('preco', 'qtde')



@admin.register(Perfil)
class perfilAdm(admin.modelAdmin):
    list_display = ('id', 'telefone', 'rua', 'numero', 'cidade')



@admin.register(Venda)
class perfilAdm(admin.modelAdmin):
    list_display = ('id', 'telefone', 'rua', 'numero', 'cidade')


@admin.register(Perfil)
class perfilAdm(admin.modelAdmin):
    list_display = ('id', 'telefone', 'rua', 'numero', 'cidade')

