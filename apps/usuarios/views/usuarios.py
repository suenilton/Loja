from django.shortcuts import render, redirect
from usuarios.models import *

def login(request):
    return render(request, 'usuarios\login.html')
