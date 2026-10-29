print("1) Cuadrado\n2) Triangulo\n\n")
numero= int(input("Introduzca un número: "))

if numero == 1:
    lado = int(input("Introduzca un lado del cuadrado: "))
    areaCuadrado = lado * 4
    print("El area del cuadrado es de:", areaCuadrado)
elif numero == 2:
    base = int(input("Introduzca la base del triangulo: "))
    altura = int(input("Introduzca la altura del triangulo: "))
    
    areaTriangulo = base * altura
    
    print("El area del triangulo es de:",areaTriangulo)
else:
    print("Introduzca una opcion válida")