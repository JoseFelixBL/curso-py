import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_N")

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola mundo",
    from_=numero,
    to="+15551111111"
)

# Al ejecutar este script se enviará el mensaje SMS a ese número
# Recordar que Twilio da número gratis de USA para USA
# Para operar en otros países hay que contratar un número de ese otro país
# y completar la info legal requerida por Twilio de dicho país
