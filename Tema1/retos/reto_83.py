correcto = 0
while correcto == 0:
    mayuscula = input("Introduzca texto en mayuscula: ")
    
    if mayuscula.isupper():
        print(mayuscula)
        correcto = 1
    else:
        print("Por favor intenta ponerlo todo en mayuscula")
        
