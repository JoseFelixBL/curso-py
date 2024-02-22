numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Ok!
# primero, segundo, tercero = numeros
primero, *otros = numeros
print(primero, otros)
