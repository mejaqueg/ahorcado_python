# Ejercicio 1

mystring = "Esta es una cadena."
print(mystring)
print(type(mystring))
print(mystring + " Es un dato de tipo " + str(type(mystring)))
# La f sigue de comillas (f"así"...
print(f"{mystring} Es un dato de tipo {str(type(mystring))}")

# Ejercicio 2

firststring = "water"
secondstring = "fall"
thirdstring = firststring + secondstring
print(thirdstring)

# Ejercicio 3

name = input("¿Cuál es tu nombre? ")
print(name)

# Ejercicio 4

color = input("¿Cuál es tu color favorito? ")
animal = input("¿Cuál es tu animal favorito? ")
print("{}, eres como un {} {}!".format(name, color, animal))
