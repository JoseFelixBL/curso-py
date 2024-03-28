import sqlite3

con = sqlite3.connect("sqlite/app.db")

# El cursor es un intermediario entre sqlite3 y nosotros para poder enviar consultas
cursor = con.cursor()

# Para ejecutar consultas: execute()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)

# Para que las consultas se lleven a cabo hay que hacer un commit
# Si no llamamos a commit NO SE REALIZA NINGÚN CAMBIO
con.commit()

# Recordar siempre cerrar la base de datos
con.close()
