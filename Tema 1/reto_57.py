import random

numAleatorio = random.randint(1,10)
acertado = 0
while acertado == 0:
    num = int(input("Introduzca el número correcto: "))
    
    if num == numAleatorio:
        print("correcto")
        acertado = 1
    elif num > numAleatorio:
        print("El numero tiene que ser mas pequeño")
    else:
        print("El número tiene que ser más grande")