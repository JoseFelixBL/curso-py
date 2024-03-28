# import time

# print(time.time())
# # Esto devuelve un TIMESTAMP (segundos desde 01-enero-1970) en UTC

# import datetime

# fecha = datetime.datetime(2024, 3, 28)
# print(fecha)

from datetime import datetime

# Formas de crear objetos de fecha
fecha = datetime(2024, 3, 28)
fecha2 = datetime(2024, 4, 28)
print(fecha, fecha2)

ahora = datetime.now()
print(ahora)

# Crear una fecha a partir de un string
# El segundo argumento se le conoce como "directives" para que python
# sepa cómo interpretar la fecha
# Para ver todas las directivas que hay buscar:
#   python 3 strptime directives  -- la URL de DATETIME
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr)

# Craer un String a partir de una fecha
print(fecha.strftime("%Y.%m.%d"))

# Comparar fechas
print(fecha > fecha2)

# Propiedades de objetos de fecha
print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
    fecha.second,
)
