numInvitados = 0
continuar = "y"
while continuar == "y":
    invitado = input("¿Como se llama la persona que quieres invitar?: ")
    print(invitado,"ha sido invitado")
    numInvitados = numInvitados + 1
    continuar = input("¿Quieres invitar a otra persona?: ")
print("El número total de personas invitadas es de", numInvitados)