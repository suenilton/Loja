from django.shortcuts import render

def carrinho_detalhado(request):
    return render(request, 'loja\carrinho\carrinho_detalhado.html')
