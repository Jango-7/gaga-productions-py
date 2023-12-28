from django.db import models

# Create your models here.
class JazzArts(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.descripcion}"
    

class BluesArts(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.descripcion}"
    

class RockArts(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.descripcion}"