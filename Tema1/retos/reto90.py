from array import *

contador = 0
numArrays = array('i',[])


while contador < 5:
    numero = int(input("Introduce un numero entre el 10 y el 20: "))
    
    if numero > 20 or numero < 10:
        print("Número fuera de los límites")
    else:
        numArrays.append(numero)
        print("Introducido el numero",numero)
        contador += 1
        
print("Muchas gracias por introducir los 5 números")

for i in numArrays:
    print(i)