from django.db import models

class Libro(models.Model):
    # Nombre de la tabla en la Base de Datos
    titulo = models.CharField(max_length=100, default='DEFAULT VALUE')
    autor = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio1 = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock1 = models.CharField(max_length=100, default='DEFAULT VALUE')
    img1 = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'libros' 
        
class Arepa(models.Model):  #nombre de la tabla en la Base de Datos
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    #stock = models.TextChoices('Si Hay', 'No hay')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'arepas' #nombre de instancia con la que llamamos la tabla en la Base de Datos