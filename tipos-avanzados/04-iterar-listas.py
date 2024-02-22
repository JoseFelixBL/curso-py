mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

# asignaciones: primero, segundo = [1, 2]

for mascota in enumerate(mascotas):
    print(mascota)
    print(mascota[0], mascota[1])

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
