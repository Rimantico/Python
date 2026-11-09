# Hacer un programa que compruebe si una frase es palindroma o no

frase = input()
frase = frase.lower().replace(" ","")
fraseAlReves =(frase[::-1])

if fraseAlReves == frase:
    print("Son palindromas")
else:
    print("No son palindromas")