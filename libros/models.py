from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    nombre_genero = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_genero

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacion = models.IntegerField()
    stock = models.IntegerField(default=0)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    autores = models.ManyToManyField(Autor)
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    def __str__(self):
        return f'Préstamo de {self.libro.titulo} a {self.usuario.username}'
