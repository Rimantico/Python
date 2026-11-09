numInvitados = int(input("¿Cuantos invitados quieres que vengan a la fiesta?: "))

if numInvitados < 10:
    for i in range(0,numInvitados):
        invitado = input("Introduzca su nombre: ")
        print("¡",invitado,"ha sido invitado!")
else:
    print("Hay que invitar a mucha gente")