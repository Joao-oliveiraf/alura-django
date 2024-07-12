from django.shortcuts import render
from usuarios.forms import CadastroForm, LoginForm


def login(request):
    form = LoginForm()
    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {"form": form})