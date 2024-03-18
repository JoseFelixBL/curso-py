# Las propiedades de las instancias se definen con self delante
# Porque son de cada instancia.
# Las propiedades de Clases se definen sin self y todas las instancias
# acceden a una sola referencia de memoria para cada variable de clase
# o sea, si alguien cambia la propiedad de clase la cambia para todos
# p.e.: Perro.patas = 5
# si cam,bio la propiedad de la instancia, la cambio solo para la
# instancia

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
