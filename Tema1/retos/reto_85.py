nombre = input("Introduzca su nombre: ")
vocales = "aeiouáéíóú"
contador = 0

for letra in nombre.lower():
    if letra in vocales:
        contador += 1
        
print(f"Tu nombre tiene {contador} vocales")