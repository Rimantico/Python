total = 0

for i in range(0,5):
    num = int(input("Introduzca el numero: "))
    incluir = input("¿Quiere incluir este numero?: ")
    
    if incluir == "si":
        total = total + num
    else:
        print("Ese número no se incluirá")

print("El resultado con los números incluidos es",total)