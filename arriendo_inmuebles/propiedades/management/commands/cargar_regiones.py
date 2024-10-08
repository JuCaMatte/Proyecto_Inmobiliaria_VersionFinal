import csv
from django.core.management.base import BaseCommand
from propiedades.models import Region

class Command(BaseCommand):
    help = 'Carga regiones desde un archivo CSV'

    def handle(self, *args, **kwargs):
        # Abre el archivo CSV ubicado en la ruta 'data/regiones.csv'}
        # with open(file_path, 'r', encoding='utf-8') as file:
        with open("data/regiones.csv", mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Itera sobre cada fila en el archivo CSV
            for row in reader:
                codigo_reg = row['codigo_region']
                nombre_reg = row['nombre_region']

                # Crea o actualiza la región en la base de datos
                Region.objects.update_or_create(
                    codigo_region=codigo_reg,
                    defaults={'nombre': nombre_reg}
                )
        # Mensaje de éxito cuando el comando se ejecuta correctamente
        self.stdout.write(self.style.SUCCESS('Regiones cargadas exitosamente'))
