num = int(input("Dame un número por debajo de 50: "))

if num > 50:
    print("Este número es más grande que 50")
else:
    for i in range(50,num-1,-1):
        print(i)