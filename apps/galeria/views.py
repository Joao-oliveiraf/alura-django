from django.shortcuts import get_object_or_404, redirect, render
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.db.models import Q
from django.db import models
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User


def index(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Faça login ou cadastre-se para acessar a galeria!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    # messages.info(request, f'Logado como xxxx')
    return render(request, 'galeria/index.html', {"cards": fotografias,})

def imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)
    messages.info(request, f'Logado como {request.user.username.title()}')
    return render(request, 'galeria/imagem.html', {"fotografia": foto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Faça login ou cadastre-se')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if fotografias.filter(Q(nome__icontains=nome_a_buscar) | Q(legenda__icontains=nome_a_buscar)):
            fotografias = fotografias.filter(Q(nome__icontains=nome_a_buscar) | Q(legenda__icontains=nome_a_buscar))
            return render(request, 'galeria/buscar.html', {"cards": fotografias})
        elif nome_a_buscar == '':
            return render(request, 'galeria/buscar.html')
        else:
            return render(request, 'galeria/buscar.html')
def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para adicionar novas imagens')
        return redirect('login')
    
    imagem = FotografiaForms
    if request.method == 'POST':

        imagem = FotografiaForms(request.POST) # HttpRequest.POST A dictionary-like object containing all given HTTP POST parameters

        if imagem.is_valid():
            imagem.save()
            messages.success(request, 'Nova imagem adicionada!')
            return redirect(request, 'home')

    return render(request, 'galeria/nova-imagem.html', {'form': imagem})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass