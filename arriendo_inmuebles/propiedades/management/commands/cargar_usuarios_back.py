import csv
from django.core.management.base import BaseCommand
from propiedades.models import Usuario, TipoUsuario


class Command(BaseCommand):
    help = "Carga usuarios desde un archivo CSV"

    # ef add_arguments(self, parser):
    #    parser.add_argument("data/users.csv", type=str)

    def handle(self, *args, **kwargs):
        # archivo_csv = kwargs["data/users.csv"]
        with open('data/users.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                try:
                    Usuario.objects.update_or_create(
                        rut=row["rut"],
                        defaults={
                            #'username': row['username'],
                            "username": row["username"],
                            "first_name": row["first_name"],
                            "last_name": row["last_name"],
                            "direccion": row["direccion"],
                            "telefono": row["telefono"],
                            "email": row["email"],
                        },
                    )
                except Exception as e:
                    self.stderr.write(f'Error al procesar fila {row}: {e}')
        self.stdout.write(self.style.SUCCESS("Usuarios cargados exitosamente"))
