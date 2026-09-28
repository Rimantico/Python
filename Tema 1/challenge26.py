palabra = input("Introduzca una palabra").lower()

vocales = "aeiuou"

if palabra[0] in vocales:
    resultado = palabra+ "way"
else:
    resultado = palabra[1:] + palabra[0] + "ay"
    
print("En Latin sería:",resultado)