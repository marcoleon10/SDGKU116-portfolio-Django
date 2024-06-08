from django.db import models


class Articulo(models.Model):
    seccion = models.CharField(max_length=100)
    contenido = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.seccion

