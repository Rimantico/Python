num = []

for i in range(0,3):
    numero = int(input("Introduce un número: "))
    num.append(numero)
    
seguir = input("¿Quieres continuar?: ")

if seguir == "no":
    longitud = len(num)
    num.pop()
    print(num)
else:
    numero = int(input("Introduce un número: "))
    num.append(numero)