from urllib.parse import urlparse
from django.urls import path
from .views import carrinho_detalhado

app_name = 'carrinho'

urlpatterns =[
    path('', carrinho_detalhado, name='carrinho_detalhado'),
]