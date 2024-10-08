from django.core.management.base import BaseCommand
from propiedades.models import Usuario, TipoUsuario


class Command(BaseCommand):
    help = "Carga usuarios desde un archivo CSV"

    def handle(self, *args, **kwargs):
        import csv

        with open("data/usuarios.csv", newline="") as csvfile:
            #reader = csv.DictReader(csvfile)
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                try:
                    tipo_usuario_codigo = row.get("tipo_usuario", "").strip()

                    # Buscar el tipo de usuario por el código proporcionado
                    tipo_usuario = TipoUsuario.objects.get(codigo=tipo_usuario_codigo)

                    usuario = Usuario(
                        rut=row["rut"].strip(),
                        first_name=row["first_name"].strip(),
                        last_name=row["last_name"].strip(),
                        email=row["email"].strip(),
                        direccion=row["direccion"].strip(),
                        tipo_usuario=tipo_usuario,  # Asignar la relación con TipoUsuario
                    )
                    usuario.set_password(row["password"].strip())
                    usuario.save()

                except TipoUsuario.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f"TipoUsuario con código {tipo_usuario_codigo} no existe. Fila: {row}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error al procesar fila {row}: {e}")
                    )

        self.stdout.write(self.style.SUCCESS("Usuarios cargados exitosamente"))
