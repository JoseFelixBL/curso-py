numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True,)
print(numeros)
print(numeros2)

usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]
usuarios.sort()
print(usuarios)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

usuarios.sort()
print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)
# print(usu_ord)

# usuarios.sort(key=ordena, reverse=True)
# usuarios.sort(key=lambda parametros: contenidoDeLaFunción, reverse=True)
# usuarios.sort(key=lambda parametros: valorRetorno, reverse=True)
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
