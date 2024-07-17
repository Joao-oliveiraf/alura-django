from django.shortcuts import get_object_or_404, redirect, render
from galeria.models import Fotografia
from django.db.models import Q
from django.contrib import messages


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
    