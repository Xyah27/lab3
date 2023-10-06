"""
URL configuration for libro_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from libro_app import AutorListado, LibroListado, AutorDetalle, LibroDetalle, AutorCrear, LibroCrear, AutorActualizar, LibroActualizar, AutorEliminar, LibroEliminar
urlpatterns = [
    path('admin/', admin.site.urls),  
    
    # La ruta 'leer' en donde listamos todos los registros o arepas de la Base de Datos
    path('arepas/', AutorListado.as_view(template_name = "arepas/index.html"), name='leer'),
    path('arepas/', LibroListado.as_view(template_name = "arepas/index.html"), name='leer'),
    

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un arepas o registro 
    path('arepas/detalle/<int:pk>', AutorDetalle.as_view(template_name = "arepas/detalles.html"), name='detalles'),
    path('arepas/detalle/<int:pk>', LibroDetalle.as_view(template_name = "arepas/detalles.html"), name='detalles'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo arepas o registro  
    path('arepas/crear', AutorCrear.as_view(template_name = "arepas/crear.html"), name='crear'),
    path('arepas/crear', LibroCrear.as_view(template_name = "arepas/crear.html"), name='crear'),
    

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un arepas o registro de la Base de Datos 
    path('arepas/editar/<int:pk>', AutorActualizar.as_view(template_name = "arepas/actualizar.html"), name='actualizar'), 
    path('arepas/editar/<int:pk>', LibroActualizar.as_view(template_name = "arepas/actualizar.html"), name='actualizar'), 
    

    # La ruta 'eliminar' que usaremos para eliminar un arepas o registro de la Base de Datos 
    path('arepas/eliminar/<int:pk>', AutorEliminar.as_view(), name='eliminar'),   
    path('arepas/eliminar/<int:pk>', LibroEliminar.as_view(), name='eliminar'),   
    
]

