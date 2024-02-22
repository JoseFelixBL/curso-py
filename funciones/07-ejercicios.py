def quitar_blancos(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def voltear(texto):
    al_reves = ""
    # for n in range(len(texto)):
    #     al_reves += texto[-1 - n]
    for char in texto:
        al_reves = char + al_reves
    return al_reves


def es_palindromo(texto):
    # sin_blancos = quitar_blancos(texto.lower())
    sin_blancos = quitar_blancos(texto)
    volteado = voltear(sin_blancos)
    # resultado = True
    # for n in range(len(sin_blancos)):
    #     if sin_blancos[n] != volteado[n]:
    #         resultado = False
    # return resultado
    return sin_blancos.lower() == volteado.lower()


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Somos o no somos", es_palindromo("Somos o no somos"))
