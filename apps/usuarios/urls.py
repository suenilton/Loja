from django.urls import URLPattern, path
from .views import *

app_name = 'usuarios'

urlpatterns =[
    path('login', login, name='login'),
]