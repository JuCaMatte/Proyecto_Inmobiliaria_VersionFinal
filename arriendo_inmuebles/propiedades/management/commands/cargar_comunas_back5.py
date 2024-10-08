import csv
from django.core.management.base import BaseCommand
from propiedades.models import Comuna, Region


class Command(BaseCommand):
    help = "Cargar comunas desde un archivo CSV"

    def handle(self, *args, **kwargs):
        file_path = "data/comunas.csv"

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=";")

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Nombres de columnas en el CSV: {reader.fieldnames}"
                    )
                )

                for row in reader:
                    nombre_comuna = row.get("Nombre Comuna")
                    codigo_region = row.get("Código Región desde 2018")

                    if not nombre_comuna or not codigo_region:
                        self.stdout.write(
                            self.style.ERROR(f"Datos incompletos en la fila: {row}")
                        )
                        continue

                    region, created = Region.objects.get_or_create(
                        pk=codigo_region,
                        defaults={"nombre": row.get("Nombre Región desde 2018")},
                    )

                    Comuna.objects.create(
                        nombre=nombre_comuna,
                        region=region,
                    )

                    self.stdout.write(
                        self.style.SUCCESS(f"Comuna {nombre_comuna} cargada con éxito.")
                    )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocurrió un error: {e}"))
