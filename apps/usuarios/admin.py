from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from usuarios.models import *
from .forms import UsuarioChangeForm, UsuarioCreationForm


@admin.register(Usuario)
class UserAdmin(auth_admin.UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    model = Usuario
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Campos personalizados', {'fields': ('campoextra',)}),
    )
