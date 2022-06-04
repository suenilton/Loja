from django.urls import URLPattern, path
from .views import *

app_name = 'roupas'

urlpatterns =[
    path('', home, name='home'),
    path('produtos', produtos, name='produtos'),
    path('categoria/<slug:slug>/', produtos, name='produtos_por_categoria'),
    path('produtos/<slug:slug>/', produto_detalhado, name='produtos_detalhados'),
]