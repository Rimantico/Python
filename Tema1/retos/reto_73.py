colores=["Rojo","Amarillo","Azul","Rosa","Verde","Morado","Lila","Naranja","Blanco","Negro"]
comienzoIntervalo = int(input("Introduzca un número entre 0 y 4: "))

if comienzoIntervalo < 0 or comienzoIntervalo > 4:
    print("Introduzca un número valido")
else:
    finalIntervalo = int(input("Introduzca un número entre 5 y 9: "))
    
    if finalIntervalo < 5 or finalIntervalo > 9:
        print("Introduzca un número valido")
    else:
        print(colores[comienzoIntervalo:finalIntervalo])