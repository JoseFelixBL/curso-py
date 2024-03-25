if __name__ != "__main__":

    # from ..gestion.crud import guardar #IMPORT RELATIVO
    from usuarios.gestion.crud import guardar  # IMPORT ABSOLUTO

    print(__name__)

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()


if __name__ == "__main__":
    print("Ejecutar tareas de mantenimiento")
