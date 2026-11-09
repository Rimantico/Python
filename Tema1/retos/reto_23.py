cancion = input("Dime el principio de una canción infantil: ")
inicio = int(input("Dime donde quieres que corte: "))
final = int(input("Dime donde quieres que termine: "))

print(cancion[inicio:final])