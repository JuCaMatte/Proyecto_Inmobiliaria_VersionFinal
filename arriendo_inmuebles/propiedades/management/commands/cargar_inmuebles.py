import csv
from django.core.management.base import BaseCommand
from propiedades.services import crear_propiedad


class Command(BaseCommand):
    help = "Cargar propiedades desde un archivo CSV"

    def handle(self, *args, **kwargs):
        file_path = "D:/Areas de estudio/Curso Praxis/BootCamp FullStack Python/M7/Proyecto-Hito2-Migraciones-Recuperacuion_datos/arriendo_inmuebles/data/inmuebles.csv"

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)  # Salta la primera línea de cabecera
            for fila in reader:
                print(f"Leyendo fila: {fila}")
                try:
                    print(
                        f"Intentando crear propiedad con los siguientes datos: {fila}"
                    )
                    propiedad = crear_propiedad(
                        fila[0],  # nombre
                        fila[1],  # descripcion
                        fila[2],  # tamaño
                        fila[3],  # estacionamientos
                        fila[4],  # habitaciones
                        fila[5],  # baños
                        fila[6],  # direccion
                        fila[7],  # comuna_nombre
                        fila[8],  # tipo
                        fila[9],  # precio_arriendo
                    )
                    print(
                        f"Propiedad creada con éxito: {propiedad.nombre} - {propiedad.id}"
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error al crear la propiedad: {e}")
                    )
