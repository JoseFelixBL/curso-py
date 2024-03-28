import os
from pathlib import Path
import sys

# sys.argv nos muestra los argumentos que le pasamos a la función desde la línea de
# comandos, siendo el primer argumento el nombre de la función
# print(sys.argv)

# Vamos a crear una función que renombre un fichero


def cli(args):
    # primero validar que hay más de un argumento
    if len(args) == 1:
        print("no se pasaron argumentos")
        return
    # Comprobar que nos han pasado 2 argumentos
    if len(args) != 3:
        print("se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("el destino no puedee existir")
        return

    os.rename(origen, destino)
    print("Archivo renombrado con éxito")


# El scrip, cuando sea llamado desde la línea de comandos, podrá recibir argumentos
# para ejecutar la función cli
cli(sys.argv)
