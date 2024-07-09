from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia


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
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            return render(request, 'galeria/buscar.html', {"cards": fotografias})
        elif nome_a_buscar == '':
            return render(request, 'galeria/buscar.html')
    