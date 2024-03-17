class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")


class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Perro(Caminador, Nadador):
    def pasear(self):
        print("paseando al perro")


class Chanchito(Perro, Animal):
    def programar(self):
        print("programando")


chanchito = Chanchito()
chanchito.pasear()
