# Cuando tenemos una lista y necesitamos rescatar un dato
# podemos hacerlo así:

animales = ["Sr. Maní", "Tocino", "Minino"]

print(animales[0])

# PEERO!! En una lista con muchos animales, no me sirve esta función y aquí entran los bucles:
# bucle for:

# # for animal in animales:
#     if animal == "Tocino":
#         print("Si está el tocino")
#     else:
#         print("No está el tocino")


# bucle while:

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# Metodos

Nombre = "sirius cloud"

Nombre2 = Nombre.upper()
Nombre3 = Nombre.lower()
Nombre4 = Nombre.title()
Nombre5 = Nombre.capitalize()

print(Nombre)
print(Nombre2)
print(Nombre3)
print(Nombre4)
print(Nombre5)
