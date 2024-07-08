from django.shortcuts import render


def index(request):
    dados_da_imagem = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1079",
            "legenda":"nasa.org / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards": dados_da_imagem})

def imagem(request):
    return render(request, 'galeria/imagem.html')
