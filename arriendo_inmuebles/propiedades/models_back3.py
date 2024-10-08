from django.db import models
from django.contrib.auth.models import AbstractUser


class Region(models.Model):
    codigo_region = models.CharField(max_length=10, unique=True, default="00")
    nombre = models.CharField(
        max_length=100, unique=True, help_text="Nombre de la región"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ["nombre"]


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_comuna = models.AutoField(primary_key=True)
    codigo_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class TipoInmueble(models.Model):
    codigo = models.CharField(max_length=10, unique=True, primary_key=True, default="0")
    nombre = models.CharField(
        max_length=100, unique=True, help_text="Nombre de tipo de inmueble"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Inmueble"
        verbose_name_plural = "Tipos de Inmuebles"


class TipoUsuario(models.Model):
    codigo = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(
        max_length=50, unique=True, help_text="Nombre de tipo de Usuario"
    )
    usuarios = models.ManyToManyField(
        "Usuario", related_name="tipos_usuario", blank=True
    )

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    rut = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username


class Arriendo(models.Model):
    # Fields definition
    pass


class Inmueble(models.Model):
    codigo = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    baños = models.IntegerField()
    habitaciones = models.IntegerField()
    estacionamientos = models.IntegerField()
    descripcion = models.TextField()
    comuna = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, related_name="inmuebles"
    )
    tipo = models.ForeignKey(
        TipoInmueble, on_delete=models.CASCADE, related_name="inmuebles"
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="inmuebles"
    )

    def __str__(self):
        return f"{self.nombre} - {self.comuna.nombre}, {self.comuna.region.nombre}"
