class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error: tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por ir {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)  # la instancia no debería guardar
Usuario.buscar_por_id(123)  # el que debería guardar es la clase
