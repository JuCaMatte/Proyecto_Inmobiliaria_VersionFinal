import csv
from django.core.management.base import BaseCommand
from propiedades.models import Comuna, Region

# Se ejecuta usando python manage.py test_client


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open("data/comunas.csv", "r", encoding="utf-8")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)  # Se salta la primera linea
        for fila in reader:
            Comuna.objects.create(nombre=fila[0], codigo=fila[1], region_id=fila[3])