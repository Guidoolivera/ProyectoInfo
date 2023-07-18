from django.urls import path
from .views import ArticuloView
from . import views

app_name = 'apps.articulos'


urlpatterns = [
    #path('articulos', articulos, name = 'articulos'),
    path ('articulos/', ArticuloView.as_view(), name = 'articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name="leer_articulo"),
    ]
