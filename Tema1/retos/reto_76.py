listaInvitados = []

for i in range(0,3):
    invitado=input("Introduzca el nombre del invitado: ")
    listaInvitados.append(invitado)
    
continuar=input("¿Quieres continuar invitando gente?: ")


if continuar == "no":
    print("La lista de invitados es la siguiente:",listaInvitados)
else:
    while continuar != "no":
        invitado = input("Introduzca el nombre del invitado: ")
        listaInvitados.append(invitado)
        continuar = input("¿Quieres continuar invitando gente?: ")
        

print("La lista de invitados es la siguiente:",listaInvitados)