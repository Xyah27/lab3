from django.shortcuts import render
from .models import Autor, Libro
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class AutorListado(ListView):
    model = Autor
class LibroListado(ListView):
    model = Libro

class AutorCrear(SuccessMessageMixin, CreateView):
    model = Autor
    form = Autor
    fields = "__all__"
    success_message = 'Autor creado exitosamente'
    def get_success_url(self):
        return reverse('leer')
class LibroCrear(SuccessMessageMixin, CreateView):
    model = Libro
    form = Libro
    fields = "__all__"
    success_message = 'Libro creado exitosamente'
    def get_success_url(self):
        return reverse('leer')
    
class AutorDetalle(DetailView):
    model = Autor
class LibroDetalle(DetailView):
    model = Libro
 
class AutorActualizar(SuccessMessageMixin, UpdateView):
    model = Autor
    form = Autor
    fields = "__all__"
    success_message = 'Autor actualizado exitosamente'
    def get_success_url(self):
        return reverse('leer')   
class LibroActualizar(SuccessMessageMixin, UpdateView):
    model = Libro
    form = Libro
    fields = "__all__"
    success_message = 'Libro actualizado exitosamente'
    def get_success_url(self):
        return reverse('leer')

class AutorEliminar(SuccessMessageMixin, DeleteView):
    model = Autor
    form = Autor
    fields = "__all__"
    def get_success_url(self):
        success_message = 'Autor eliminado exitosamente'
        messages.success (self.request, (success_message))
        return reverse('leer')   
class LibroEliminar(SuccessMessageMixin, DeleteView):
    model = Libro
    form = Libro
    fields = "__all__"
    def get_success_url(self):
        success_message = 'Libro eliminado exitosamente'
        messages.success (self.request, (success_message))
        return reverse('leer')   