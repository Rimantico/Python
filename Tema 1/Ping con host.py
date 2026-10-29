import os
from datetime import datetime
import subprocess

# Aplicación hecha por Juan Gómez Ruiz


##Con esto formatearemos la fecha que queramos poner
fechaActual = datetime.now()
fecha_formateada = fechaActual.strftime("%d/%m/%Y %H:%M")


print("Análisis ejecutado:",fecha_formateada)
print("------------------------------------")


# Con este comando abriremos el archivo de host.txt en forma de lectura y accederemos a el mediante la variable archivo
with open("host.txt","r") as archivo:
    direcciones = archivo.read().splitlines()
    
    for ip in direcciones:
        #Con esto haremos que capture lo que nos de el ping
        resultado = subprocess.run(["ping",ip],capture_output=True,text= True)
        
        #Aqui lo que haremos será que en el caso de que resultado salga la palabra TTL entonces estará bien y la página estará up, Si no aparece es que esta down
        if "TTL=" in resultado.stdout.upper():
            print(f"{ip}---> El host está up")
        else:
            print(f"{ip}---> El host está down")
            
print("------------------------------------")