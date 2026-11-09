lluvia = input("¿Esta lloviendo?: ")
lluvia = str.lower(lluvia)
if lluvia == "si":
    viento = input("¿Hace viento?: ")
    viento = str.lower(viento)
    if viento == "si":
        print("Hace mucho viento para un paraguas")
    else:
        print("Coge un paraguas")
else:
    print("Disfruta de tu dia")