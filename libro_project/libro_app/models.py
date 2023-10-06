from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100, default='DEFAULT VALUE')
    autor = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'libros'  # Nombre de la instancia con la que llamamos la tabla en la Base de Datos

class Autor(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    nacionalidad = models.CharField(max_length=100, default='DEFAULT VALUE')
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'autores'  # Nombre de la instancia con la que llamamos la tabla en la Base de Datos
