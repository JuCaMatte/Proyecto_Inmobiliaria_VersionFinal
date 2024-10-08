# from .models import Comuna, Propiedad, Usuario, Arriendo
from .models import Comuna, Inmueble, Usuario, Arriendo

# Crear una nueva propiedad
# def crear_propiedad(
#    nombre,
#    descripcion,
#    tamaño,
#    estacionamientos,
#    habitaciones,
#    baños,
#    direccion,
#    comuna,
#    tipo,
#    precio_arriendo,
# ):
#    propiedad = Propiedad(
#        nombre=nombre,
#        descripcion=descripcion,
#        tamaño=tamaño,
#        estacionamientos=estacionamientos,
#        habitaciones=habitaciones,
#        baños=baños,
#        direccion=direccion,
#        comuna=comuna,
#        tipo=tipo,
#        precio_arriendo=precio_arriendo,
#    )
#    propiedad.save()
#    return propiedad


def crear_propiedad(
    nombre,
    descripcion,
    tamaño,  # Asegúrate de que este nombre coincida con el campo del modelo
    estacionamientos,
    habitaciones,
    baños,
    direccion,
    comuna_nombre,  # Renombrado para indicar que es el nombre de la comuna
    tipo,
    precio_arriendo,
):
    try:
        # Buscar o crear la instancia de Comuna basada en el nombre
        comuna_instance = Comuna.objects.get(nombre=comuna_nombre)
    except Comuna.DoesNotExist:
        raise ValueError(f"La comuna '{comuna_nombre}' no existe.")

    # Crear la nueva propiedad
    # propiedad = Propiedad(
    propiedad = Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        tamaño=tamaño,
        estacionamientos=estacionamientos,
        habitaciones=habitaciones,
        baños=baños,
        direccion=direccion,
        comuna=comuna_instance,  # Usar la instancia de Comuna
        tipo=tipo,
        precio_arriendo=precio_arriendo,
    )

    # Guardar la propiedad en la base de datos
    propiedad.save()

    return propiedad


# Leer una propiedad por su ID
def obtener_propiedad(id):
    # return Propiedad.objects.get(id=id)
    return Inmueble.objects.get(id=id)

# Actualizar una propiedad existente
def actualizar_propiedad(id, **kwargs):
    #propiedad = Propiedad.objects.get(id=id)
    propiedad = Inmueble.objects.get(id=id)
    for key, value in kwargs.items():
        setattr(propiedad, key, value)
    propiedad.save()
    return propiedad


# Borrar una propiedad
def borrar_propiedad(id):
    # propiedad = Propiedad.objects.get(id=id)
    propiedad = Inmueble.objects.get(id=id)
    propiedad.delete()
