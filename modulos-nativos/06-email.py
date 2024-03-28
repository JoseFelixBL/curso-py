# Para poder enviar correos desde gmail hay que habilitar less secure apps
# https://myaccount.google.com/u/1/lesssecureapps
# Para crear las partes del correo
from email.mime.multipart import MIMEMultipart
# Para poder escribir el cuerpo del mensaje
from email.mime.text import MIMEText
# Para poder adjunta una imagen al correo
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib  # para poder referenciar el servidor gmail

path = Path("modulos-nativos/Jelly_fish_ok.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Jfb Adds"
mensaje["to"] = "tu_correo@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

# Crear la referencia al servidor SMPT, como hay que cerrarla, usamos "with"
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # Esto nos identifica con el servidor smtp y el nombre de dominio que vamos a utilizar para enviar los correos
    smtp.starttls()  # para que la información viaje encriptada; TLS Transport Layer Security

    smtp.login("mi_cuenta@gmail.com", "mi_email_pass")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
