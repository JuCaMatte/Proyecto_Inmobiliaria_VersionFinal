import csv
from django.core.management.base import BaseCommand
from propiedades.models import Usuario
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = "Carga los usuarios desde un archivo CSV"

    def handle(self, *args, **kwargs):
        with open("data/users.csv", mode="r", encoding="utf-8") as file:
            # reader = csv.DictReader(file)
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                try:
                    Usuario.objects.create(
                        rut=row["rut"],  # Se usa 'rut' en lugar de 'username'
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        email=row["email"],
                        password=make_password(
                            row["password"]
                        ),  # Hashing de la contraseña
                        direccion=row["direccion"],
                    )
                except Exception as e:
                    self.stderr.write(f"Error al procesar fila {row}: {e}")
        self.stdout.write(self.style.SUCCESS("Usuarios cargados exitosamente"))
