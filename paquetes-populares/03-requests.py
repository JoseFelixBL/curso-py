
import requests

# La siguiente URL es la API a la que nos vamos a conectar
# El resultado de la conexión es una lista de diccionarios
# donde cada diccionario contiene un usuario
# "https://api.holamundo.io/users/"

# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout=10)
# # print(r.status_code,
# #       r.text
# # )
# r = r.json()

# for user in r:
#     # print(user["name"])
#     print(user["name"])

# url = "https://jsonplaceholder.typicode.com/users/7"
# r = requests.get(url, timeout=10)
# !!! nos está devolviendo bien el campo, pero es un texto... no lo he convertido de json...
# print(r.text)
# print(r.json())

# url = "https://jsonplaceholder.typicode.com/users"
# user = {
#     "name": "Chanchito feliz"
# }
# r = requests.post(url, timeout=10, data=user)
# print(r.status_code)

# url = "https://jsonplaceholder.typicode.com/users/2"
# user = {
#     "name": "Chanchito feliz"
# }
# r = requests.put(url, timeout=10, data=user)
# print(r.status_code)

# url = "https://jsonplaceholder.typicode.com/users/2"

# r = requests.delete(url, timeout=10)
# print(r.status_code)

# HEADERS en APIKey
url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "123456"
headers = {
    "Authorisation": f"Bearer {apikey}"
}

r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)
