from django.urls import path
from .views import inicio, otra_vista, numero_random, nombre_del_usuario, mi_plantilla

urlpatterns = [
    path('inicio/', inicio),
    path('', otra_vista),
    path('numero-random/', numero_random),
    path('dame-numero/<numero>', nombre_del_usuario),
    path('mi-plantilla/', mi_plantilla),  
]
