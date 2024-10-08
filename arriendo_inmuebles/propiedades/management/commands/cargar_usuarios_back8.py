import csv
import os
import django
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from propiedades.models import (
    TipoUsuario,
)  # Ajusta este import según tu estructura de proyecto

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "propiedades.settings")
django.setup()


class Command(BaseCommand):
    help = "Cargar usuarios desde un archivo CSV"

    def handle(self, *args, **kwargs):
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
                tipo_usuario_id = fila["tipo_usuario"]

                # Crear un nombre de usuario a partir del nombre y apellido
                username = f"{first_name.lower()}.{last_name.lower()}"

                if password != password_confirm:
                    print(
                        f"Error al procesar fila {fila}: Las contraseñas no coinciden."
                    )
                    continue

                try:
                    # Obtener el tipo de usuario
                    tipo_usuario = TipoUsuario.objects.get(codigo=tipo_usuario_id)

                    # Obtener el modelo de usuario personalizado
                    Usuario = get_user_model()

                    # Verificar si el usuario ya existe
                    user, created = Usuario.objects.get_or_create(username=username)

                    if created or user:
                        # Si el usuario fue creado, establecer sus atributos
                        user.first_name = first_name
                        user.last_name = last_name
                        user.email = email
                        user.set_password(password)
                        user.save()
                        print(
                            f"Usuario {username} {'creado' if created else 'actualizado'} con éxito."
                        )
                    else:
                        print(
                            f"Error al procesar fila {fila}: No se pudo crear o actualizar el usuario."
                        )

                    # Asociar el usuario con el tipo de usuario
                    #tipo_usuario.usuarios.add(user)
                    user.tipo_usuario = tipo_usuario
                    user.save()
                except TipoUsuario.DoesNotExist:
                    print(
                        f"Error al procesar fila {fila}: Tipo de usuario con código {tipo_usuario_id} no encontrado."
                    )
                except Exception as e:
                    print(f"Error al procesar fila {fila}: {e}")
