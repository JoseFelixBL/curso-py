from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("guandando en archivo")


# def guardar(entidad):
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
# guardar(usuario)

sesion = Sesion()
# guardar(sesion)
guardar([usuario, sesion])
