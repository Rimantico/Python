# Hecho por: Juan Gómez Ruiz

# UN PEQUEÑO INCISO:
# Cuando estaba realizando esta práctica la estaba realizando en Ubuntu y no en Linux, no se si podría afectar en algo

# Parte de imports

import os
import subprocess
import smtplib
from email.message import EmailMessage
from getpass import getpass

# Código Principal

print(os.getcwd())

# Voy a escribir tres direcciones IP, una la loopback ,con la que estoy conectado a mi dispositivo y una aleatoria

with open("host.txt","w",) as archivo:
    archivo.write("127.0.0.1\n")
    archivo.write("192.168.0.136\n")
    archivo.write("192.168.3.121\n")
    
    
# Ahora guardaré las direcciones en una lista o en un array

direcciones = []

with open("host.txt","r",) as leerArchivo:
    for i in leerArchivo:
        direcciones.append(i.strip("\n"))

# Para comprobar de que se ha guardado correctamente la dirección lo pasaremos por pantalla
print(direcciones)

# Una vez que ya tenemos las direcciones bien separadas y sin nigún caracter adicional podemos hacer el ping

comprobacionEstado = []

for x in direcciones:
    estado = subprocess.run(["ping","-c","3","-W","3", x],stdout=subprocess.DEVNULL)
    
    if estado.returncode == 0:
        comprobacionEstado.append("UP")
        print(x,"está UP")
    else:
        comprobacionEstado.append("DOWN")
        print(x,"está DOWN")
        
# Una vez que ya tenemos las direcciones, procederemos a ver en que estado están:

print(comprobacionEstado)

# Ahora tendremos que ver que IP esta DOWN de forma más gráfica

direccionesCaidas = []

for ip, estado in zip(direcciones,comprobacionEstado):
    if estado == "DOWN":
        print("La dirección",ip,"está down")
        direccionesCaidas.append(ip)
        
        
# Por último con este if si tenemos direcciones caídas me mandará un correo en donde estaŕan las direcciones que no estan UP
# La clave es privada y cada vez que queramos mandar el coreo nos pedirá el código 
if direccionesCaidas:
    mensaje = EmailMessage()
    mensaje["Subject"] = "Aviso: direcciones IP sin respuesta"
    mensaje["From"] = "jgomrui1410@gmail.com"
    mensaje["To"] = "jgomrui1410@gmail.com"
    mensaje.set_content(
        "Estas IP no responden:\n" + "\n".join(direccionesCaidas)
    )

    clave = getpass("Contraseña de aplicación de Gmail: ")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(mensaje["From"], clave)
        servidor.send_message(mensaje)

    print("Correo enviado")