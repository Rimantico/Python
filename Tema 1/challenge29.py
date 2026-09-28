import math
numero = int(input("Introduce un número mayor a 500: "))

if numero > 500:
    numero = math.sqrt(numero)
    print("La raiz cuadrada es:",round(numero,2))
else:
    print("El número no es mayor que 500")