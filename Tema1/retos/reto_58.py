import random

print("Quiz matematico")
numAcertados =0
for i in range(0,5):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
        resultado = num1 + num2
    
    print(num1,"+",num2,"=")
    
    respuesta = int(input("¿Cual es tu respuesta?: "))
    
    if resultado == respuesta:
        numAcertados = numAcertados+1
print("Has acertado:",numAcertados,"de 5")
    

