nombre = input("Introduzca su nombre: ")
num = int(input("Introduzca un número: "))

if num >= 10:
    for i in range(0,3):
        print("Muy alto el numero")
else:
    for i in range(0,num):
        print(nombre)