# Calculadora
# Interactiva
# si no hay número, pedir que ingrese un número
# si hay número, pedir que ingrese operación
# pedir segundo número
# Hacer la operación, mostrar resultado y poner el resultado como primer número
# ir a pedir que ingrese operación...
# Las operaciones son: suma, resta, multi y div
# Para salir escribe: Salir

print("Bienvenidos a la calculadora")
print("Las operaciones son: suma, resta, multi y div")
print("Para salir escriba: Salir")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida.")
        break
    print(f"El resultado es {resultado}")

print("Hasta luego")
