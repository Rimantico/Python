lista = []

for i in range(0,2):
    deporte= input("Introduce tu deporte favorito: ")
    lista.append(deporte)
    
lista.sort()

print("La lista de deportes favoritos es:",lista)