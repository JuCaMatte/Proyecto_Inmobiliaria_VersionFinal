# from django.urls import admin
# from django.contrib import admin
# from django.urls import path, include
from django.urls import path

from django.contrib import admin
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', views.inicio, name='index'),  # Ruta para la página de inicio
    path("propiedad/crear/", views.crear_propiedad_view, name="crear_propiedad"),
    path("propiedad/<int:id>/", views.detalle_propiedad_view, name="detalle_propiedad"),
    path(
        "propiedad/<int:id>/actualizar/",
        views.actualizar_propiedad_view,
        name="actualizar_propiedad",
    ),
    path(
        "propiedad/<int:id>/borrar/",
        views.borrar_propiedad_view,
        name="borrar_propiedad",
    ),
    path(
        "propiedades/listar/", views.listar_propiedades_view, name="listar_propiedades"
    ),  
    path(
        'contacto/', views.contacto_view, name='contacto'
    ),  # Asegúrate de que esta línea esté presente
    # path(
    #    "contacto/", include("contactos.urls")
    # ),  # Si 'contactos' es el nombre de la aplicación que maneja la vista de contacto
    # path("admin/", admin.site.urls),
    # path("propiedades/", include("propiedades.urls")),
    # path("", include("propiedades.urls")),
]
