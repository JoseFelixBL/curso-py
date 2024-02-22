usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# modificar una lista - map
# nombres = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]

# filtrar una lista - filter
# nombres = [expresion for item in items if condicion]

nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# modificar y filtrar a la vez
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Usando MAP y FILTER
# nombres = list(map(lambda usuario: usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
nombres = list(map(lambda usuario: usuario[0], menosUsuarios))
print(nombres)
