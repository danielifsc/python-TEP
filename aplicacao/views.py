from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import login_required 

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contatos(request):
    context = {'telefone' : '2050-2050', 'email' : 'carlinhos@gmail.com'}
    return render(request, 'contatos.html', context)
def produto(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produto.html", context)
# Create your views here.

def cadastrarProduto(request):
    return render(request, "cadastrarProduto.html")

def salvarProduto(request):
    get_object_or_404(Produto, id=id)

    thisnome = request.POST.get('txtNome')  
    thispreco = request.POST.get('txtPreco').replace(',','.')   
    thisqtde = request.POST.get('txtQtde') 
    thisdescricao = request.POST.get('txtDescricao')
    thisdata = request.POST.get('txtData')

    produto = Produto(
        nome = thisnome,
        preco = float(thispreco),
        qtde = thisqtde,
        descricao = thisdescricao,
        data = thisdata

    )

    produto.save()
    return redirect('urlproduto')

def editarProduto(request, id):

    produto = get_object_or_404(Produto, id=id)

    if request.method == "GET":
        context = {'p': produto}
        return render(request, "editarProduto.html", context)
    else:
        teste = request.POST.get('txtPreco').replace(',','.')
        produto.nome = request.POST.get('txtNome')  
        produto.preco = float(teste)  
        produto.qtde = request.POST.get('txtQtde') 
        produto.descricao = request.POST.get('txtDescricao')
        produto.data = request.POST.get('txtData')

        produto.save()
        return redirect('urlproduto')

def excluirProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('urlproduto')

def entrar(request):
    
    if request.method == "GET":
        return render(request, "entrar.html")
    else:
        return HttpResponse('entrou')