from statistics import quantiles


class Carrinho():
    def __init__(self, request):
        if request.session.get('carrinho') is None:
            request.session['carrinho'] = {}
        
        self.carrinho = request.session['carrinho']
    
    def add(self, product):
        self.carrinho[str(product.id)] = {
            'quantity' : 1,
            'price' : str(product.price),
        }