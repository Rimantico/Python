from array import *
import random

numArrays = array('i',[])

for i in range(0,5):
    numeroAleatorio = random.randint(1,100)
    numArrays.append(numeroAleatorio)
    
for x in numArrays:
    print(x)
    