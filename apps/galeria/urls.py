from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem,editar_imagem, deletar_imagem


urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova-imagem'),
    path('editar-imagem', editar_imagem, name='editar-imagem'),
    path('deletar-imagem', deletar_imagem, name='deletar-imagem')
]