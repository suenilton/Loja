from django.shortcuts import render, redirect
from roupas.models import * 

def home(request):
    conjuntos = ConjuntoRoupas.objects.order_by('-data_conjunto').filter(status_conjunto=True)

    dados = {
        'conjuntos': conjuntos
    }
    
    return render(request, 'loja\home.html', dados)

def produtos(request):
    produtos = Produto.objects.order_by('-data_produto').filter(status_produto=True)
    # produtos = Produto.objects.all()
    dados = {
        'produtos': produtos
    }
    
    return render(request, 'loja\produtos.html', dados)
