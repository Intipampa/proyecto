from django.contrib import admin
from .models import Genero, Autor, Libro, Prestamo

admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamo)
