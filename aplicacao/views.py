from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

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
    thisnome = request.POST.get('txtNome')  
    thispreco = request.POST.get('txtPreco').replace(',','.')   
    thisqtde = request.POST.get('txtQtde') 
    thisdescricao = request.POST.get('txtDescricao')
    thisdata = request.POST.get('txtData')

    produto.nome = thisnome
    produto.preco = float(thispreco)
    produto.qtde = thisqtde
    produto.descricao = thisdescricao
    produto.data = thisdata

    produto.save()
    return redirect('urlproduto')

def editarProduto(request, id):
    if request.method == "GET":
        context = {'p': produto}
        return render(request, "editarProduto.html", context)
    else:

      thisnome = request.POST.get('txtNome')  
      thispreco = request.POST.get('txtPreco').replace(',','.')  
      thisqtde = request.POST.get('txtQtde') 
      thisdescricao = request.POST.get('txtDescricao')
      thisdata = request.POST.get('txtData')

      produto.nome = thisnome
      produto.preco = float(thispreco)
      produto.qtde = thisqtde
      produto.descricao = thisdescricao
      produto.data = thisdata

    produto.save()
    return redirect('urlproduto')

def excluirProduto(request, id):
    if request.method == "GET":
        context = {'p': produto}
        return render(request, "excluirProduto.html", context)
    else:

      thisnome = request.POST.get('txtNome')  
      thispreco = request.POST.get('txtPreco').replace(',','.')   
      thisqtde = request.POST.get('txtQtde') 
      thisdescricao = request.POST.get('txtDescricao')
      thisdata = request.POST.get('txtData')

      produto.nome = thisnome
      produto.preco = float(thispreco)
      produto.qtde = thisqtde
      produto.descricao = thisdescricao
      produto.data = thisdata
 
    produto.save()
    return redirect('urlproduto')