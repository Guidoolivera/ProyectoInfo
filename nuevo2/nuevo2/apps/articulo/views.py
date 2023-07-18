from django.shortcuts import render
from .models import Articulo
from django.views import View

#Vista basada en función
def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulo.html',{'articulos' : articulos})

#Vista basada en clases
class ArticuloView(View):
    template_name = 'articulo.html'

    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'articulo.html',{'articulos' : articulos})