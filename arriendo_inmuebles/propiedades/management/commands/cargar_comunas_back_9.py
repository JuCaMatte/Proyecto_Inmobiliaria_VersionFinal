import csv
from django.core.management.base import BaseCommand
from propiedades.models import Region, Comuna


class Command(BaseCommand):
    help = "Carga datos de comunas desde un archivo CSV"



    with open("comunas_y_regiones.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            region, created = Region.objects.get_or_create(
                nombre=row["Nombre Región desde 2018"],
                codigo_region=row["Código Región desde 2018"],
            )
            Comuna.objects.create(
                nombre=row["Nombre Comuna"],
                codigo_comuna=row["Código Comuna desde 2018"],
                region=region,
            )
