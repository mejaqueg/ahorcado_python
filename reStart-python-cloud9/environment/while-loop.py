import random

print("¡Bienvenido a adivina el número!")
print("Las reglas son simples. Yo pienso un número y tu tratas de adivinarlo")

number = random.randint (1,10)

isGuessRight = False
while isGuessRight != True:
    guess = input ("Avivina un número entre el 1 y el 10: ")
    if int(guess) == number:
        print("Tu dijiste {}. ¡Es correcto! ¡Tú ganas!".format(guess))
        isGuessRight = True
    else:
        print("Tú dijiste {}. Lo siento, no era. Intentalo otra vez".format(guess))
    