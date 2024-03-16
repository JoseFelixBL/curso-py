"""Ver si una palabra es palíndrome"""


def es_palindromo_old(texto):
    texto_ok = texto.replace(" ", "").lower()
    # letra_atras = -1
    # for letra in texto_ok:
    #     if letra != texto_ok[letra_atras]:
    #         return False
    #     letra_atras -= 1
    # return True

    ind_al_reves = -1
    al_reves = ""
    for _ in range(len(texto_ok)):
        al_reves += texto_ok[ind_al_reves]
        ind_al_reves -= 1
    if texto_ok == al_reves:
        return True
    else:
        return False


def no_space(texto):
    sin_espacios = ""
    for char in texto:
        if char != " ":
            sin_espacios += char
    return sin_espacios


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves.lower() == texto.lower()


print(f'Hola mundo -> {es_palindromo("Hola mundo")}')
print(f'Abba -> {es_palindromo("Abba")}')
print(f'Reconocer -> {es_palindromo("Reconocer")}')
print(f'Amo la paloma -> {es_palindromo("Amo la paloma")}')
print(f'Somos o no somos -> {es_palindromo("Somos o no somos")}')
