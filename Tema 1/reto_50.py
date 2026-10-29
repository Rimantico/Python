num = 0

while num < 10 or num > 20:
    num = int(input("Introduzca un número entre el 10 y el 20: "))
    
    if num < 10:
        print("numero bajo")
    elif num > 20:
        print("numero alto")
    else:
        print("numero entre 10 y 20")