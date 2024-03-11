"""Ejercicio calculadora"""

"""
Escribe "Bienvenidos a la calculadora"
escribe "para salir escribe Salir"
escribe "Las operaciones don suma, resta, muti y div"
Verificar si se ha ingresado un número antes
    Sí --> ingrese una operación
        Sí --> ingrese otro nr.
            Sí --> mostrar resultado
                guardar resultado como 1er nr.
                ir a pedirle que ingrese operación
    NO --> ingrese un número
"""

print("Bienvenidos a la calculadora")
print("para salir escribe Salir")
print("Las operaciones don suma, resta, multi y div")

n1 = ""
while True:
    if not n1:
        while not n1.isnumeric() and n1.lower() != "salir":
            n1 = input("Ingrese un número: ")
        if n1.lower() == "salir":
            break
        n1 = int(n1)

    op = ""
    while op.lower() not in ("suma", "resta", "multi", "div", "salir"):
        op = input("Ingrese una operación: ")
    if op.lower() == "salir":
        break

    n2 = ""
    while not n2.isnumeric() and n2.lower() != "salir":
        n2 = input("Ingrese otro número: ")
    if n2.lower() == "salir":
        break

    if op.lower() == "suma":
        n1 += int(n2)
        print(f"El resultado es {n1}")
    elif op.lower() == "resta":
        n1 -= int(n2)
        print(f"El resultado es {n1}")
    elif op.lower() == "multi":
        n1 *= int(n2)
        print(f"El resultado es {n1}")
    elif op.lower() == "div":
        n1 /= int(n2)
        print(f"El resultado es {n1}")
