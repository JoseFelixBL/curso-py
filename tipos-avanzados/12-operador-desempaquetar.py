lista = [1, 2, 3, 4]
print(lista)
print(1, 2, 3, 4)
print("Lista", *lista)
tupla = (1, 2, 3, 4)
print("Tupla", *tupla)
# def kk (n1, n2, n3):  se puede llamar así kk(*lista):

lista1 = [1, 2, 3, 4]
lista2 = [5, 6]
combinada = ["Hola", *lista1, "mundo", *lista2, "Chanchito"]
print(combinada)

# Para los diccionarios se usan 2 asteriscos: **
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)
