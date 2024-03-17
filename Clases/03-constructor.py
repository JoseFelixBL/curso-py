class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Chanchito", 1)
mi_perro.habla()
# mi_perro2 = Perro("Felipe")
# print(mi_perro.nombre)
# print(mi_perro2.nombre)
