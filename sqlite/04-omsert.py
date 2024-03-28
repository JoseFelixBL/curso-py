import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()

    # Pasamos la consulta separada de los valores para prevenis SQLInjection
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Hola Mundo"),
    )
