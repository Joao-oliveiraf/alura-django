from re import U
from django.shortcuts import render,redirect
from usuarios.forms import CadastroForm, LoginForm

from django.contrib.auth.models import User # Important, User class to link with db params.
from django.contrib import auth
from django.contrib import messages


def login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect('home')
            else:
                messages.error(request, 'Erro ao logar!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):

    form = CadastroForm()

    if request.method == 'POST':

        form = CadastroForm(request.POST) # HttpRequest.POST A dictionary-like object containing all given HTTP POST parameters

        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'Senhas não são iguais!')
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            username_already_exists = User.objects.filter(username=nome).exists()
            
            if username_already_exists:
                messages.error(request, 'Senhas não são iguais!')
                return redirect('cadastro')
            else:
                new_user = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha,
                    is_active=1,
                    is_staff=0
                )
                new_user.save()
                messages.success(request, 'Usuário criado com sucesso!')
                return redirect('login')
    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logout efetuado com sucesso!')
        return redirect('login')
    else:
        messages.success(request, 'Nenhum usuário logado!')
        return redirect('login')