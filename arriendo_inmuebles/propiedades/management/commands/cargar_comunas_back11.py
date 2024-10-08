import csv
from django.core.management.base import BaseCommand
from propiedades.models import Comuna


class Command(BaseCommand):
    help = "Carga datos de comunas desde un archivo CSV"

    def handle(self, *args, **kwargs):
        try:
            with open("data/comunas.csv", "r", encoding="utf-8") as file:
                # reader = csv.reader(file)
                reader = csv.reader(
                    file, delimiter=";"
                )  # Especifica el delimitador ';'
                header = next(reader)  # Lee y omite la primera fila (encabezado)
                for row_number, row in enumerate(reader):
                    if len(row) < 2:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Fila {row_number + 2} tiene menos de 2 columnas"
                            )
                        )
                        continue

                    try:
                        codigo_comuna = int(row[0])  # Asegúrate de convertir a entero
                        nombre = row[1]
                        Comuna.objects.create(
                            codigo_comuna=codigo_comuna, nombre=nombre
                        )
                    except ValueError as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Error al procesar fila {row_number + 2}: {e}"
                            )
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Error al procesar fila {row_number + 2}: {e}"
                            )
                        )

            self.stdout.write(self.style.SUCCESS("Datos cargados exitosamente"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Archivo CSV no encontrado"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al abrir el archivo: {e}"))
