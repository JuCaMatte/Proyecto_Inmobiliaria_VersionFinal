from django.db import models


class Region(models.Model):
    #id = models.CharField(max_length=10, primary_key=True)  # Ajusta el max_length si es necesario
    #nombre = models.CharField(max_length=100)
    
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    
    
    # Otros campos relevantes...

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    # nombre = models.CharField(max_length=255)
    # cod = models.CharField(max_length=50)  # O el tipo de campo que corresponda
    # region = models.ForeignKey(
    #    Region, on_delete=models.CASCADE
    # )  # O el tipo de campo que corresponda

    nombre = models.CharField(max_length=100)
    # codigo = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10, default="0000")  # Ejemplo para CharField
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, default=1
    )  # Asegúrate de que el valor 1 corresponda a una región existente

    # Otros campos...
    def __str__(self):
        return self.nombre


class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = "tipo_inmueble"


class Propiedad(models.Model):

    #TIPO_CHOICES = [
    #    ('casa', 'Casa'),
    #    ('departamento', 'Departamento'),
    #    ('oficina', 'Oficina'),
    #    ('terreno', 'Terreno'),
    #]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tamaño = models.DecimalField(max_digits=5, decimal_places=2)
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    #tipo = models.CharField(max_length=50)  # Ej. Casa, Departamento
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = (
        ("arrendatario", "Arrendatario"),
        ("arrendador", "Arrendador"),
    )

    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return self.nombre


class Arriendo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.propiedad}"
