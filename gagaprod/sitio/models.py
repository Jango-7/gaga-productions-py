from django.db import models

# Create your models here.
class ProduccionesMod(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    pedido = models.TextField()

    def __str__(self):
        return f"Pedido de producción para el cliente: {self.nombre}"
    
# =======================================
    

class MultitracksMod(models.Model):
    artista = models.CharField(max_length=20)
    cancion = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Multitracks del artista: {self.artista}"
    
#========================================
    

class ChartsMod(models.Model):
    artista = models.CharField(max_length=20)
    cancion = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Charts y cifrados de: {self.artista}"