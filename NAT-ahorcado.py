# Juego del ahorcado con Naty.

# Definir una palabra a adivinar.

# Número de intentos disponibles.

# Pedir una letra a la vez.

# Resultado de acierto o de pérdida.


def ahorcado():
    palabra_secreta = "barbaro"
    letras_adivinadas = []
    intentos = 5

    while intentos > 0:
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta:
            print("¡Has adivinado la palabra!")
            break
        letra_usuario = input("Ingresa una letra: ")

        # Verificar si la letra ha sido adivinada:

        if letra_usuario in palabra_secreta:
            print("¡Bien! Esa letra está en la palabra secreta")
            letras_adivinadas.append(letra_usuario)
        else:
            intentos -= 1
            print(
                f"¡Mal! Esa letra no está en la palabra secreta. Te quedan {str(intentos)} intentos")
        if intentos == 0:
            print("¡Has perdido! La palabra secreta era " + palabra_secreta)
            break


ahorcado()
print("¡Gracias por jugar!")
