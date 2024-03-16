pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo_elemento = pila.pop()
print(ultimo_elemento)
print(pila)
print(pila[-1])
pila.pop()
pila.pop()
if not pila:
    print("Pila vacía")
