from io import open

# escritura - write
# texto = "Hola mundo!"

# archivo.write(texto)
# archivo.close()

# lectura - read
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista - readlines
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# archivo = open("archivos/hola-mundo.txt", "r")
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())  # esto carga todo el archivo en memoria
#     archivo.seek(0)
#     for linea in archivo:  # esto carga en memoria línea por línea
#         print(linea)

# Agregar
# archivo = open("archivos/hola-mundo.txt", "+a")
# archivo.write("Chao mundo :(")
# archivo.close()

# Lectura y escritura simultáneamente
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz la"
    print(texto)
    archivo.writelines(texto)
