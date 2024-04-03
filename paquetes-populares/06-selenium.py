# ¡No poner de nombre de archivo "selenium.py"!
# Para usar variables de environment y poner en .env ewl ususario y el password
import os

# # Para importar sleep a ver si ayuda con lo de 2 step validation
# import time

# webdriver: Para crear un instancia que nos permita manipular el explorador web
from selenium import webdriver

# By: para poder tener todas las formas de buscar elementos en mi browser
from selenium.webdriver.common.by import By

# Para importar las TECLAS especiales a marcar, p.e.: RETURN
from selenium.webdriver.common.keys import Keys

# Para que Chrome no se cierre al terminar y así poder ver qué ha pasado:
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()

# Para que espera 10 segundos en cada pg nueva
# antes de arrojar un error de no encontrado
browser.implicitly_wait(10)
browser.get("https://github.com")

# Ahora buscamos el elemento "Sign in" para pinchar/click en él
# en este caso usamos selectores de CSS (HTML)
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

# Ahora rellenaremos los campos de nombre de usuario y contraseña
user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

# Ahora le indico a esas variables que quiero que ingresen texto
# user_input.send_keys("holamundo")
# pass_input.send_keys("holamundo")
user_input.send_keys(os.environ.get("gh_user"))
pass_input.send_keys(os.environ.get("gh_pass"))

# Hay que indicar dar a ENTER , pero el caracter ENTER/RETURN no se encuentra
# disponible, así que importamos la clase
pass_input.send_keys(Keys.RETURN)

# time.sleep(15)

# Ahora tenemos que validar que llegamos a donde queríamos
# buscando nuestro nombre en un elemento HTML de la web
# En mi caso hay que pinchar en el botón (avatar circle) primero
# Para que se abra un menú lateral que contiene mi nombre de usuario
avatar_button = browser.find_element(
    By.CLASS_NAME,
    "AppHeader-logo.Button--invisible.Button--medium.Button.Button--invisible-noVisuals.color-bg-transparent.p-0"
)
avatar_button.send_keys(Keys.RETURN)

# Buscar mi perfil
profiles = browser.find_elements(
    By.CLASS_NAME,
    "Truncate-text"
)

user = os.environ.get("gh_user")
user_ok = False
for p in profiles:
    if p.get_attribute("innerHTML").strip() == user:
        # print("¡Eureka!")
        user_ok = True
        break

if not user_ok:
    print("No se encontró el usuario. Terminando.")
    browser.quit()

print("Sí, estoy en el usuario correcto 😁👍🏽")

# p.send_keys(Keys.ESCAPE)

# close_button = browser.find_element(
#     By.CLASS_NAME,
#     "AppHeader-logo.Button--invisible.Button--medium.Button.Button--invisible-noVisuals.color-bg-transparent.p-0"
# )
# "close-button.Overlay-closeButton"

# close_button.click()

# time.sleep(10)
browser.quit()
