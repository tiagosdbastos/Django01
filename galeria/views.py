from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia


def index(request):
    fotos = Fotografia.objects.all()

    return render(request, 'galeria/index.html', {"cards": fotos})

def imagem(request, id):
    foto = get_object_or_404(Fotografia, pk=id)
    return render(request, 'galeria/imagem.html', {"foto": foto})