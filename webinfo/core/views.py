from django.shortcuts import render
from .models import peliculas


# todo vista basada en funcion que me permite mostrar un template(HTML)
def index(request):
    template_name = "index.html"
    # context = {
    #     "reseña": "El Perro Basquetbolistas(2008)",
    #     "puntuacion": "4 de 5 estrellas",
    #     "director": "Armando Ruiz",
    #     "descripcion": "Aunque no se incluyen los 150 minutos de un partido de campeonato completo,",
    #     "tapa": "https://tse3.mm.bing.net/th?id=OIP.Z6uW2ree03AcBFcGo2N-rwHaKl&pid=Api&P=0"
    # }
    # todo select * from peliculas
    # ORM = object relation mapping
    pls = peliculas.objects.all()
    # todo select * from peliculas where id=1
    # pls = peliculas.objects.get(pk=1)
    context = {
        "peliculas": pls
    }
    return render(request, template_name, context)


def detalles(request, id_pelicula=None):
    template_name = "detalle.html"
    pel = peliculas.objects.get(pk=id_pelicula)
    context = {
        "pelicula": pel
    }
    #print(context)
    return render(request, template_name, context)

