programas=["The good doctor","The rookie","Arcane","La que se avecina"]

for i in range(0,4):
    print(programas[i])
    
nuevoPrograma = input("Introduzca un nuevo programa: ")
posicion = int(input("Introduzca la posición en la que quieras introducir el programa: "))

programas.insert(posicion,nuevoPrograma)

print(programas)