from django.shortcuts import render, redirect, get_object_or_404
from roupas.models import *

def home(request):
    conjuntos = ConjuntoRoupas.objects.order_by('-data_conjunto').filter(status_conjunto=True)
    # for conjunto in conjuntos:
    #     print(conjunto.nome_produtos_do_conjunto.all())
        
    dados = {
        'conjuntos': conjuntos
    }
    
    return render(request, 'loja\home.html', dados)

def produtos(request, **kwargs):
    categoria = None
    produtos = Produto.objects.order_by('-data_produto').filter(status_produto=True)
    categorias = Categoria.objects.all()
    categoria_slug = kwargs.get('slug')
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = produtos.filter(categoria_produto=categoria)
    context = {
        'produtos': produtos,
        'categorias': categorias
    }
    
    return render(request, 'loja\produtos.html', context)

def produto_detalhado(request, **kwargs):
    produto_slug = kwargs.get('slug')
    produto_detalhado = get_object_or_404(Produto, slug=produto_slug)

    context = {
        'produto': produto_detalhado
    }
    return render(request, 'loja\produto_detalhado.html', context)
