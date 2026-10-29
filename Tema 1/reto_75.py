listaNumeros = [132,245,253,653]

for i in range(0,4):
    print(listaNumeros[i])
    
numero = int(input("Introduce un número: "))

if numero in listaNumeros:
    print("Este número esta dentro de la lista")
else:
    print("Este número no esta en la lista")
    listaNumeros.append(numero)
    print("La lista actualizada es:",listaNumeros)