import sqlite3

# Generar una conexión con la DDBB app.db
con = sqlite3.connect("sqlite/app.db")

# Siempre tenemos que recordar cerrar la DDBB, si no lo hacemos
# no podremos volver a escribir en esa DDBB
con.close()
