# El signo = está asignando el algo, pero no significa que sea "igual".
# El signo == sería el "igual".

nombre = "Miguel"

print(nombre)

# Funciones:
# Todas las funciones parten con def.


def saludo():
    apellido = "Jaque"
    print("Saludos " + nombre + " " + apellido)


saludo()


# Función de suma:

numero1 = input("Introduce un número: ")
numero2 = input("Introduce otro número: ")


def suma():
    resultado = int(numero1) + int(numero2)
    print(resultado)


suma()
