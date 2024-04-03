# Variables de entorno
# SENDGRID_API_KEY

import os
# Para poder crear el mail
from sendgrid.helpers.mail import Mail
# Módulo para conectarnos a la API de SENDGRID
from sendgrid import SendGridAPIClient

email = os.environ.get("SENDGRID_EMAIL")
# print(apikey)

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="Correo de prueba",
    html_content="Curso de <b>Ultimate Python</b>"
)

# Ahora nos conectaremops a la API para enviar este mensaje
try:
    apikey = os.environ.get("SENDGRID_API_KEY")
    # Creamos el servidor
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body,
        respuesta.headers
    )
except Exception as e:
    print(e)
