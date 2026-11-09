paises = ["España","Alemania","Inglaterra","Polonia","Suiza"]

print("La lista de paises es:",paises)

nombrePais= input("Dime el nombre del pais y te diré en que posición está: ")
print("La posición del país en la tupla es:",paises.index(nombrePais))
tuplaPais = int(input("Dime la posición que quieras y te diré el país que está en la tupla: "))
print("El país que esta en esa posición es:",paises[tuplaPais])