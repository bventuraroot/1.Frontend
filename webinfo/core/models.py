from django.db import models


class peliculas(models.Model):
    resenia = models.CharField(max_length=50)
    puntuacion = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True)
    contenido= models.CharField(max_length=40, blank=True)
    #imagen = models.ImageField(upload_to="tapas/",blank=True)
    imagen = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    sipnosis= models.TextField(blank=True)
    lugar= models.CharField(max_length=20,blank=True)
    horario = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.resenia
