import csv
from django.core.management.base import BaseCommand
from propiedades.models import TipoInmueble


class Command(BaseCommand):
    help = "Carga tipos de inmuebles desde un archivo CSV"

    def handle(self, *args, **kwargs):
        # Abre el archivo CSV ubicado en la ruta 'data/regiones.csv'}
        # with open(file_path, 'r', encoding='utf-8') as file:
        with open("data/tipo_inmuebles.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",")
            # Itera sobre cada fila en el archivo CSV
            for row in reader:
                codigo = row["codigo"]
                nombre = row["tipo_inmueble"]

                # Crea o actualiza el tipo de inmueble en la base de datos
                TipoInmueble.objects.update_or_create(
                    codigo_inm  = codigo, defaults={"nombre": nombre}
                )
        # Mensaje de éxito cuando el comando se ejecuta correctamente
        self.stdout.write(self.style.SUCCESS("Regiones cargadas exitosamente"))
