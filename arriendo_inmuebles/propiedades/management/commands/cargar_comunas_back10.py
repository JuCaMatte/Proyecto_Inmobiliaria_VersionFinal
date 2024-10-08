import csv
from django.core.management.base import BaseCommand
from propiedades.models import Comuna


class Command(BaseCommand):
    help = "Carga datos de comunas desde un archivo CSV"

    def handle(self, *args, **kwargs):
        # Actualiza la ruta del archivo CSV si es necesario
        try:
            with open('data/comunas.csv', 'r', encoding='utf-8') as file:
                header = next(reader)  # Lee y omite la primera fila (encabezado)
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    # Asumiendo que el archivo CSV tiene columnas para el modelo Comuna
                    Comuna.objects.create(codigo_comuna=row[0], nombre=row[1])
            self.stdout.write(self.style.SUCCESS("Datos cargados exitosamente"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Archivo CSV no encontrado"))
