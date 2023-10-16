from django.shortcuts import render
from .models import Arepa , Libro
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



class ArepaListado(ListView):
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    
class ArepaCrear(SuccessMessageMixin, CreateView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Arepa Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class ArepaDetalle(DetailView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    
class ArepaActualizar(SuccessMessageMixin, UpdateView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Arepa Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Arepa 

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ArepaEliminar(SuccessMessageMixin, DeleteView): 
    model = Arepa 
    form = Arepa
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Arepa Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
    #VIEWS DEL 2DO MODELO
    
class LibroListado(ListView):
    model = Libro

class LibroCrear(SuccessMessageMixin, CreateView):
    model = Libro
    fields = "__all__"
    success_message = 'Libro Creado Correctamente!'

    def get_success_url(self):
        return reverse('lista_libros')  # Reemplaza 'lista_libros' con la vista principal de la lista de libros

class LibroDetalle(DetailView):
    model = Libro

class LibroActualizar(SuccessMessageMixin, UpdateView):
    model = Libro
    fields = "__all__"
    success_message = 'Libro Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('lista_libros')  # Reemplaza 'lista_libros' con la vista principal de la lista de libros

class LibroEliminar(SuccessMessageMixin, DeleteView):
    model = Libro
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Libro Eliminado Correctamente!'
        messages.success(self.request, success_message)
        return reverse('lista_libros')