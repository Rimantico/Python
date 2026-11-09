compnum = 50

print("Adivina el número")
intento = "y"
adivinado = 0
contadorIntentos = 0
while adivinado == 0:
    num = int(input("Introduzca un número: "))
    
    if num > 50:
        print("El numero es mayor")
        intento = input("¿Quieres intentarlo de nuevo?: ")
        contadorIntentos = contadorIntentos + 1
    elif num < 50:
        print("El número es menor")
        intento = input("¿Quieres intentarlo de nuevo?: ")
        contadorIntentos = contadorIntentos +1
    else:
        contadorIntentos = contadorIntentos +1
        print("Este es el número")
        adivinado = 1
        
if adivinado == 1:
    print("Has adivinado el número en",contadorIntentos,"intentos")
else:
    print("No lo has conseguido")
        
    