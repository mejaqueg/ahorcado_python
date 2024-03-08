ingreseedad = input("Ingresa tu edad: ")

edad = int(ingreseedad)

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 14:
    print("Eres un adolescente")
elif edad >= 10:
    print("Eres un niño")
else:
    print("Eres un bebe poposeado")


# Corregir: Hay un error. El input no devuelve un número, sino una cadena de texto.
