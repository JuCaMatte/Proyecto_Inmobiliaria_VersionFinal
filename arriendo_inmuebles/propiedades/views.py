from django.shortcuts import render, get_object_or_404, redirect
# from .models import Comuna, Propiedad, Usuario, Arriendo
from .models import Comuna, Inmueble, Usuario, Arriendo
# from .forms import PropiedadForm
from .forms import InmuebleForm
from .services import (
    #crear_propiedad,
    #obtener_propiedad,
    #actualizar_propiedad,
    #borrar_propiedad,
    
    crear_propiedad,
    obtener_propiedad,
    actualizar_propiedad,
    borrar_propiedad,
    
)
from django.contrib import messages
# from .forms import ContactForm
from .forms import ContactoForm

def index_view(request):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    return render(request, "index.html", {"propiedades": propiedades})


# def contacto_view(request):
#    propiedades = Propiedad.objects.all()
#    return render(request, "contacto.html", {"propiedades": propiedades})
def contacto_view(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        #form = ContactoForm()
        if form.is_valid():
            # Procesa el formulario (por ejemplo, enviar un correo o guardar en la base de datos)
            # Puedes usar form.cleaned_data para acceder a los datos del formulario
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]

            # Aquí podrías enviar un correo o guardar el mensaje en la base de datos
            # Por ejemplo, enviar un correo (esto requiere configuración adicional)
            # send_mail('Contacto', mensaje, email, ['destinatario@example.com'])

            # Agregar un mensaje de éxito
            messages.success(request, "¡Tu mensaje ha sido enviado con éxito!")
            return redirect(
                "contacto"
            )  # Redirige para evitar el reenvío del formulario
    else:
        # form = ContactForm()
        form = ContactoForm()

    return render(request, "contacto.html", {"form": form})


def inicio(request):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    return render(request, "index.html", {"propiedades": propiedades})


def crear_propiedad_view(request):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    if request.method == "POST":
        # form = PropiedadForm(request.POST)
        form = InmuebleForm(request.POST)
        if form.is_valid():
            propiedad = form.save()
            return redirect("detalle_propiedad", id=propiedad.id)
    else:
        # form = PropiedadForm()
        form = InmuebleForm()
    return render(
        request, "crear_propiedad.html", {"form": form, "propiedades": propiedades}
    )


def detalle_propiedad_view(request, id):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    # propiedad = get_object_or_404(Propiedad, id=id)
    propiedad = get_object_or_404(Inmueble, id=id)
    return render(
        request,
        "detalle_propiedad.html",
        {"propiedad": propiedad, "propiedades": propiedades},
    )


def actualizar_propiedad_view(request, id):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    # propiedad = get_object_or_404(Propiedad, id=id)
    propiedad = get_object_or_404(Inmueble, id=id)
    if request.method == "POST":
        # form = PropiedadForm(request.POST, instance=propiedad)
        form = InmuebleForm(request.POST, instance=propiedad)
        if form.is_valid():
            propiedad = form.save()
            return redirect("detalle_propiedad", id=propiedad.id)
    else:
        # form = PropiedadForm(instance=propiedad)
        form = InmuebleForm(instance=propiedad)
    return render(
        request, "actualizar_propiedad.html", {"form": form, "propiedades": propiedades}
    )


def borrar_propiedad_view(request, id):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    if request.method == "POST":
        borrar_propiedad(id)
        return redirect("listar_propiedades")
    return render(
        request,
        "borrar_propiedad.html",
        {"propiedad_id": id, "propiedades": propiedades},
    )


def listar_propiedades_view(request):
    # propiedades = Propiedad.objects.all()
    propiedades = Inmueble.objects.all()
    return render(request, "listar_propiedades.html", {"propiedades": propiedades})
