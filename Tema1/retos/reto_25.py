nombre = input("Introduzca su nombre: ")

if len(nombre) < 5:
    apellido = input("Su nombre es pequeño, introduzca un apellido: ")
    nombreCompleto = nombre+apellido
    print(nombreCompleto.upper())
else:
    print(nombre.lower())