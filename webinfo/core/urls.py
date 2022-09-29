from django.urls import path
from .views import index, detalles

urlpatterns = [
    path('', index, name='index'),
    path('detalles/<int:id_pelicula>', detalles, name='detalles')

]