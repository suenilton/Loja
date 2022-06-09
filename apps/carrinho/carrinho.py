class Carrinho():
    def __init__(self, request):
        request.session['carrinho'] = {}