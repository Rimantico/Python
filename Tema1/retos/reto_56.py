import random

numAleatorio = random.randint(1,10)
acertado = 0
while acertado == 0:
    num = int(input("Introduzca el número correcto: "))
    
    if num == numAleatorio:
        print("correcto")
        acertado = 1
    else:
        print("Incorrecto")