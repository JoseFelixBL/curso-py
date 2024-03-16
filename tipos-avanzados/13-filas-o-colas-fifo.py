from collections import deque
# lista = [1, 2, 3, 4]
# En python es ineficiente quitar el primer elemento de una lista

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
if not fila:
    print("Fila vacía")
else:
    print(fila)
