from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia
from django.db.models import Q


def index(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": foto})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "test" in request.GET:
        nome_a_buscar = request.GET['test']
        if fotografias.filter(Q(nome__icontains=nome_a_buscar) | Q(legenda__icontains=nome_a_buscar)):
            fotografias = fotografias.filter(Q(nome__icontains=nome_a_buscar) | Q(legenda__icontains=nome_a_buscar))
            return render(request, 'galeria/buscar.html', {"cards": fotografias})
        elif nome_a_buscar == '':
            return render(request, 'galeria/buscar.html')
        else:
            return render(request, 'galeria/buscar.html')
    