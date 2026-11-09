continuar = "y"
total = 0
while continuar == "y":
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    total = total + num1 + num2
    continuar= input("¿Quieres continuar?: ")
print("El total de toda la suma de números es de",total)