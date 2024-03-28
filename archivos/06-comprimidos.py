from pathlib import Path
from zipfile import ZipFile

# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     # Estamos en el directorio curso-py
#     for path in Path().rglob("*.*"):
#         # print(path.as_posix())
#         if str(path.as_posix()) != "archivos/comprimidos.zip":
#             zip.write(path)
#             # print(f"---Sí---{str(path)}")

with ZipFile("archivos/comprimidos.zip") as zip:
    # Lista los nombres de todos los archivos dentro de este zip
    # print(zip.namelist())

    # Para tener información de un archivo específico
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )

    # Para extraer los archivos en un directorio específico
    zip.extractall("archivos/descomprimidos")
