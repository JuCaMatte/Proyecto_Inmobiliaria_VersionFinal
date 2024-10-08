import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
# from django.db.utils import IntegrityError
from propiedades.models import TipoUsuario

class Command(BaseCommand):
    help = "Carga usuarios desde un archivo CSV"

    def handle(self, *args, **kwargs):
        try:
            with open("data/usuarios.csv", newline="") as csvfile:
                # reader = csv.DictReader(csvfile)
                reader = csv.DictReader(csvfile, delimiter=";")
                for row in reader:
                    try:
                        # Verificar tipo de usuario
                        tipo_usuario_id = row["tipo_usuario"]

                        # En revision : tipo_usuario = TipoUsuario.objects.get(id=tipo_usuario_id)
                        tipo_usuario = TipoUsuario.objects.get(codigo=tipo_usuario_id)

                        # Crear usuario
                        user = User.objects.create_user(
                            username=row["first_name"].lower()
                            + "."
                            + row["last_name"].lower(),
                            first_name=row["first_name"],
                            last_name=row["last_name"],
                            email=row["email"],
                            password=row["password"],
                        )
                        # Asignar tipo de usuario (si es necesario)
                        # user.tipo_usuario = tipo_usuario
                        # user.save()

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Usuario {user.username} creado correctamente"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f"Error al procesar fila {row}: {e}")
                        )
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Archivo usuarios.csv no encontrado"))
