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

numero1 = int(input("Ingresa numero: "))

while True:
    operacion = input("Ingresa operación: ")
    if operacion.lower() == "salir":
        break
    numero2 = int(input("Ingresa segundo número: "))
    if operacion.lower() == "suma":
        numero1 += numero2
    elif operacion.lower() == "resta":
        numero1 -= numero2
    elif operacion.lower() == "multi":
        numero1 *= numero2
    elif operacion.lower() == "div":
        numero1 /= numero2
    print(f"El resultado es {numero1}")

print("Hasta luego")
