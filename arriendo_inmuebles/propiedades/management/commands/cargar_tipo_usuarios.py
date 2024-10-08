import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from propiedades.models import (
    TipoUsuario,
)  # Asegúrate de que la ruta del modelo es correcta


class Command(BaseCommand):
    help = "Cargar los datos del archivo tipo_usuarios.csv en la tabla TipoUsuario"

    def handle(self, *args, **kwargs):
        # Ruta al archivo tipo_usuarios.csv
        file_path = Path("data/tipo_usuarios.csv")

        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Crear un nuevo objeto TipoUsuario por cada fila en el CSV
                TipoUsuario.objects.create(codigo=row["codigo"], nombre=row["nombre"])

        self.stdout.write(
            self.style.SUCCESS("Datos de TipoUsuario cargados exitosamente.")
        )
