#definir um contador
contador = 0
#pedir ao usuario que digite um numero
num = int(input('digite um numero:'))
if num < 2:
    print(f'{num} não é primo')
else:
    for i in range(2,num):
        if num % i == 0:
            contador += 1
    if contador == 0 :
        print('esse numero e primo')
    else: 
        print(f'esse numero não é primo e é divisível {contador} vezes')