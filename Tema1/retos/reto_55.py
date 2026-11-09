import random

juego = ["cara","cruz"]
aleatorio = random.randint(0,1)

maquina = juego[aleatorio]

opcion = input("¿cara o cruz?: ")

if maquina == opcion:
    print("Has ganado")
else:
        print("Has perdido")
        print("Habia salido",maquina)