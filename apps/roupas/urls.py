from django.urls import URLPattern, path
from .views import *

urlpatterns =[
    path('', home, name='home'),
    path('produtos', produtos, name='produtos'),
]