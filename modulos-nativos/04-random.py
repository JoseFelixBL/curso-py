import random
import string  # Para tener los caracteres a-z A-Z ... para generar una clave aleatoria

# shuffle() para desordenar una lista, puede ser un string. In place!
lista = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=3),
    random.choices("abcdefgh", k=3),
    "".join(random.choices("abcdefgh,.1234567890!~€¬", k=8))
)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
# print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)
