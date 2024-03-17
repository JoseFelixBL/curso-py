class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


Perro.patas = 3
mi_perro = Perro("Chanchito", 1)
mi_perro2 = Perro("Felipe", 1)
print(Perro.patas)
mi_perro.patas = 55
print(mi_perro.patas)
print(mi_perro2.patas)
