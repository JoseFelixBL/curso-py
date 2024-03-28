import json
from pathlib import Path

# # escribir json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"}
# ]

# # Usamos lib. json para transformar un listado de diccionarios en un json
# data = json.dumps(productos)
# # print(data) # Se ve exactamente igual que los listados y los diccionarios

# # Crear archivo con los datos de mis productos
# Path("archivos/productos.json").write_text(data)

# leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")

# Ahora transformamos esta data a un listado de diccionarios
productos = json.loads(data)
# print(productos)

# Modificar json, usando la parte de leer json
productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))
