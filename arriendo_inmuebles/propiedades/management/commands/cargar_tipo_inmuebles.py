import csv
from django.core.management.base import BaseCommand
from propiedades.models import TipoInmueble


class Command(BaseCommand):
    help = "Carga tipos de inmueble desde un archivo CSV"

    def handle(self, *args, **kwargs):
        # Abre el archivo CSV ubicado en la ruta 'data/tipo_inmueble.csv'
        with open("data/tipo_inmuebles.csv", mode="r", encoding="utf-8") as file:
            # reader = csv.DictReader(file)
            reader = csv.DictReader(file, delimiter=",")
            # Itera sobre cada fila en el archivo CSV
            for row in reader:
                codigo = row.get("codigo")
                nombre = row.get("nombre")

                try:
                    # Crea o actualiza el tipo de inmueble en la base de datos
                    TipoInmueble.objects.update_or_create(
                        codigo=codigo, defaults={"nombre": nombre}
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error al procesar fila {row}: {e}")
                    )

        # Mensaje de éxito cuando el comando se ejecuta correctamente
        self.stdout.write(self.style.SUCCESS("Tipos de inmueble cargados exitosamente"))
