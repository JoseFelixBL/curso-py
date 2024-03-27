persona = {
    "nombre": "José",
    "apellido": "Bello",
    "edad": 61,
    "genero": "M"
}


def prueba(apellido, edad, **otros):
    print(apellido, edad)
    print(otros)


prueba(**persona)
