from django.urls import path
from .views import index
from .views import contatos
from .views import produto
from .views import cadastrarProduto
from .views import salvarProduto
from .views import editarProduto
from .views import excluirProduto
from .views import entrar
from .views import sair
from .views import cadastrarUsuario

urlpatterns = [
    path('', index, name="urlindex"),
    path('contatos', contatos, name="urlcontatos"),
    path('produto', produto, name="urlproduto"),
    path('cadastrarProduto', cadastrarProduto, name="urlcadastrarProduto"),
    path('salvarProduto', salvarProduto, name="urlsalvarProduto"),
    path('editarProduto/<int:id>', editarProduto, name="urleditarProduto"),
    path('excluirProduto/<int:id>', excluirProduto, name="urlexcluirProduto"),
    path('entrar', entrar, name="urlEntrar"),
    path('sair', sair, name="urlSair"),
    path('cadastrarUsuario', cadastrarUsuario, name="urlcadastrarUsuario"),
]
