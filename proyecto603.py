# Elegir un número del 1 al 100, si la máquina elige uno mayor gana.

import random

print("Bienvenido al proyecto603. Tendrás que elegir un número aleatorio, si yo elijo uno mayor gano, de lo contrario tú ganas.")
print("Para salir solo escribe: salir")
print("¿Listo?")

numero = ""

while True:
    if not numero:
        numero = input("Escribe un número del 1 al 100: ")
        if numero.lower() == "salir":
            print("¡Gracias por jugar!")
            break
        numero = int(numero)

        numero_aleatorio = random.randint(1, 100)
        print("La máquina eligió el número: " + str(numero_aleatorio))

        if numero_aleatorio > numero:
            print("Gano la máquina :c")
            break
        elif numero_aleatorio == numero:
            print("¡Wow! Es un empate")
            break
        elif numero_aleatorio < numero:
            print("¡Ganaste!")
            break
