import csv
import os
import django
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# from propiedades.models import Usuario, TipoUsuario
from propiedades.models import TipoUsuario

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "propiedades.settings")
django.setup()


class Command(BaseCommand):
    help = "Cargar usuarios desde un archivo CSV"

    def handle(self, *args, **kwargs):
        # from propiedades.models import TipoUsuario  # Importar aquí para evitar el ciclo

        csv_file = "data/usuarios.csv"  # Ruta fija al archivo CSV

        with open(csv_file, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for fila in reader:
                rut = fila["rut"]
                first_name = fila["first_name"]
                last_name = fila["last_name"]
                email = fila["email"]
                password = fila["password"]
                password_confirm = fila["password_confirm"]
                direccion = fila["direccion"]
                # tipo_usuario_id = fila["tipo_usuario"]
                tipo_usuario_codigo = fila["tipo_usuario"]

                username = f"{first_name.lower()}.{last_name.lower()}"

                if password != password_confirm:
                    print(
                        f"Error al procesar fila {fila}: Las contraseñas no coinciden."
                    )
                    continue

                try:
                    # tipo_usuario = TipoUsuario.objects.get(codigo=tipo_usuario_id)
                    # tipo_usuario = TipoUsuario.objects.get(
                    #    id=tipo_usuario_id
                    # )  # Busca por id en la base de datos

                    tipo_usuario = TipoUsuario.objects.get(codigo=tipo_usuario_codigo)

                except TipoUsuario.DoesNotExist:
                    # print(f"Error al procesar fila {fila}: Tipo de usuario con ID {tipo_usuario_id} no encontrado.")
                    print(
                        f"Error al procesar fila {fila}: Tipo de usuario con código {tipo_usuario_codigo} no encontrado."
                    )
                    continue

                username = f"{first_name.lower()}.{last_name.lower()}"

                Usuario = get_user_model()
                user, created = Usuario.objects.get_or_create(username=username)

                if created or user:
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.set_password(password)
                    user.tipo_usuario = tipo_usuario
                    user.save()
                    print(
                        f"Usuario {username} {'creado' if created else 'actualizado'} con éxito."
                        )
                else:
                    print(
                        f"Error al procesar fila {fila}: No se pudo crear o actualizar el usuario."
                        )
