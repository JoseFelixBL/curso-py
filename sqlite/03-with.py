import sqlite3

# El "with" intentará usar el método mágico del objeto con llamado __exit__()
# que se encarga de:
#   - si no existe error, llama a commit()
#   - siempre llamará a cerrar la DDBB (close())
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
