import csv
from django.core.management.base import BaseCommand
from propiedades.models import Comuna, Region


class Command(BaseCommand):
    help = "Carga comunas desde un archivo CSV"

    def handle(self, *args, **kwargs):
        with open("data/comunas.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                nombre_comuna = row.get("Nombre Comuna")
                codigo_region = row.get("Código Región desde 2018")

                try:
                    # Obtén la región correspondiente
                    region = Region.objects.get(codigo_region=codigo_region)

                    # Crea o actualiza la comuna en la base de datos
                    Comuna.objects.update_or_create(
                        nombre=nombre_comuna,
                        codigo_region=region,
                        defaults={"nombre": nombre_comuna, "codigo_region": region},
                    )
                except Region.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Error: Región con código {codigo_region} no encontrada para la comuna {nombre_comuna}."
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error al procesar fila {row}: {e}")
                    )

        self.stdout.write(self.style.SUCCESS("Comunas cargadas exitosamente"))
