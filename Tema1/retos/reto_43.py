direccion= input("Introduce una dirección(arriba o abajo): ")

direccion =direccion.lower()

if direccion == "arriba":
    num = int(input("Introduzca un número: "))
    for i in range(1,num+1):
        print(i)
elif direccion == "abajo":
    num = int(input("Introduzca un número mas pequeño que 20: "))
    if num > 20:
        print("Introduzca un número válido")
    else:
        for i in range(20,num-1,-1):
            print(i)
else:
    print("Introduzca una opción valida")