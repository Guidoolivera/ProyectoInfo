from django.urls import path
from .views import ArticuloView


urlpatterns = [
    #path('articulos', articulos, name = 'articulos'),
    path ('articulos/', ArticuloView.as_view(), name = 'articulos'),
    ]