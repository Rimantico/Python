edad = int(input("¿Cuantos años tienes?: "))

if edad >= 18:
    print("Puedes votar")
elif edad == 17:
    print("Puedes aprender a conducir")
elif edad == 16:
    print("Puedes comprar un boleto de loteria")
else:
    print("Puedes hacer truco o trato")