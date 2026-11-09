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

nombre = input("Introduzca un nombre: ")

print("Esta en la posición:",listaInvitados.index(nombre))

seguir= input("¿Quieres que siga en la fiesta esta persona?: ")

if seguir == "no":
    listaInvitados.remove(nombre)
else:
    print("No se va a borrar")