from django.db import models

# Create your models here.
class ProduccionesMod(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    pedido = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.telefono} - {self.pedido}"
    
# =======================================
    

class MultitracksMod(models.Model):
    artista = models.CharField(max_length=50)
    cancion = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.artista} - {self.cancion} - {self.descripcion}"
    
#========================================
    

class ChartsMod(models.Model):
    artista = models.CharField(max_length=50)
    cancion = models.CharField(max_length=50)
    tonalidad = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.artista} - {self.cancion} - {self.tonalidad}"