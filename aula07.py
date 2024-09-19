from time import sleep 
import os

x = int(input('digite o numero de segundos da contagem regressiva:'))
for i in range(x,-1, -1):
    os.system('cls')
    print(f'carregando {i}..')
    sleep(1)

    
print('auto destruição da máquina!')