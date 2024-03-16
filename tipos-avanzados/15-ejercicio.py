from pprint import pprint

"""	
• Ejercicio:
    a. Eliminar los espacios en blanco de un string usando list comprehension 
    y mostrar caracteres restantes
    b. Contar en un diccionario cuánto se repiten los caracteres de un string
    c. Ordenar las llaves de un diccionario por el valor que tienen y devolver 
    una lista que contenga tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]
    d. De un listado de tuplas, devolver las tuplas que tengan el mayor valor
    e. Crear un mensaje que diga:
        i. los caracteres que más se repiten  con 4 repeticiones son: y formar 
        una lista con dichos caracteres
        ii. Los caracteres tiene que estar con mayúsculas
    f. Juntar la solución de los ejercicios anteriores para encontrar los 
    caracteres que más se repiten en un string
"""


def quitar_blancos(string):
    """retornar el string sin blancos"""
    return [char for char in string if char != " "]


def contar_char(string):
    """Contar los la frecuencia de cada caracter"""
    caracteres = {}
    for char in string:
        if char not in caracteres:
            caracteres[char] = 0
        caracteres[char] += 1
    return caracteres


def ordenar_claves(diccio):
    """Mi versión - me enredé con el dict sin recordar la función sorted!!!"""
    # - pasar diccionario a lista de listas
    # - ordenar la lista con la función lambda
    # - pasar la lista de listas a lista de tuplas
    lista = []
    for letra, valor in diccio.items():
        lista += [[letra, valor]]
    lista.sort(key=lambda letra: letra[1], reverse=True)

    lista_tuplas = []
    for registro in lista:
        lista_tuplas += [tuple(registro)]
    return lista_tuplas


def ordena(dict):
    """Versión Hola Mundo"""
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def lista_tuplas_mayores(lista_t):
    """Mi versión: para devolver una lista de tuplas como decía el enunciado..."""
    l_t_m = []
    max = 0
    for letra, valor in lista_t:
        if max <= valor:
            max = valor
            l_t_m += [tuple([letra, valor])]
        else:
            break
    return l_t_m


def mayores_tuplas(lista):
    """Versión Hola mundo: devuelve un diccionario"""
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(lista_mayores):
    """Versión Hola mundo: crear el mensaje en una función"""
    mensaje = "Los que más se repiten son: \n"
    for key, valor in lista_mayores.items():
        mensaje += f"- {key.upper()} con {valor} repeticiones \n"
    return mensaje


string = "Hola mundo esto es una prueba del curso"
# print(quitar_blancos(string))
st_sin_blancos = quitar_blancos(string)
dic_frecuencia_letras = contar_char(quitar_blancos(st_sin_blancos))

pprint(dic_frecuencia_letras, width=1)
lista_tuplas_ord = ordenar_claves(dic_frecuencia_letras)
lista_t_m = lista_tuplas_mayores(lista_tuplas_ord)

_, num = lista_t_m[0]
print(
    f"Los caracteres que más se repiten con {num} repeticiones en el string:")
print(f"\"{string}\"\nson:")
for letra, valor in lista_t_m:
    print(f"\t{letra.upper()}\t{valor}")
