import csv
from django.core.management.base import BaseCommand
from propiedades.models import Comuna, Region


class Command(BaseCommand):
    help = "Carga comunas desde un archivo CSV"

    def handle(self, *args, **kwargs):
        # Abre el archivo CSV ubicado en la ruta 'data/comunas.csv'
        with open("data/comunas.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # nombre_comuna = row["nombre_comuna"]

                nombre_comuna = row['Nombre Comuna']
                # codigo_region = row["codigo_region"]
                codigo_region = row['Código Región desde 2018']

                # Obtén la región correspondiente
                try:
                    region = Region.objects.get(codigo=codigo_region)
                except Region.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Región con código {codigo_region} no encontrada"
                        )
                    )
                    continue

                # Crea o actualiza la comuna en la base de datos
                Comuna.objects.update_or_create(
                    nombre=nombre_comuna,
                    region=region,
                    defaults={"nombre": nombre_comuna},
                )
        # Mensaje de éxito cuando el comando se ejecuta correctamente
        self.stdout.write(self.style.SUCCESS("Comunas cargadas exitosamente"))
