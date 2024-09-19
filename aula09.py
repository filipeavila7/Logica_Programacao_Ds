import random 
import os
import time
tentados = []
tentativas = 10
tempo = 30
#recebe um numero aleatorio entre 0 e 100
num_premi = random.randint(0,100)
os.system('cls')
while True:
    num = int(input('digite um numero:'))
    if num == num_premi:
        print('voce ganhou')
        break
    elif tentativas == 0:
        print('acabou as tentativas! muito burro')
        break
    else:
        print('voce não acertou o numero')
        tentados.append(num)
        print(f'numeros tentados: {tentados}')
        '''for i in (tentados):
            print(f'numeros tentados:{i}')'''
        tentativas -= 1
        print(f'tentativas restantes:{tentativas}')
       

        if num > num_premi:
            print('digite um numero menor')
        else:
            print('digite um numero maior')
    
print('fim do jogo!')
print(f'voce precisou de {len(tentados)} tentativas')
print(f'numeros tentados: {tentados}')
if num != num_premi:
    print(f'o numero premiado era {num_premi}, burrao!')
else:
    print(f'o numero premiado era {num_premi}, parabens!')
    
