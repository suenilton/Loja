from django.urls import URLPattern, path
from .views import *

app_name = 'roupas'

urlpatterns =[
    path('', home, name='home'),
    path('produtos', produtos, name='produtos'),
]