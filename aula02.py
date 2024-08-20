print("------------------------------------------------")
nm = input('insira seu nome:')
print("------------------------------------------------")
email = input('insira seu email: ')
print("------------------------------------------------")
num = input('insira seu numero:')
print("------------------------------------------------")
gasolina = int(input('insira a gasolina gasta em km/l:'))
print("------------------------------------------------")
alcool = int(input('insira o alcool gasto em km/l:'))
totalkm = 1280
div = 1280 / gasolina
div2 = 1280 / alcool 
print("------------------------------------------------")
print(f'a gasolina gasta no percusso foi: {div:.3f}km/l')
print("------------------------------------------------")
print(f'o alcool gasto no percusso foi: {div2:.3f}km/l')
print("------------------------------------------------")
vlrgaso = float(input('insira o valor da gasolina:'))
print("------------------------------------------------")
vlralco = float(input('insira o valor do alcool:'))
gastogaso = div * vlrgaso
gastoalco = div2 * vlralco
print("------------------------------------------------")
print(f'o valor gasto de gasolina é:{gastogaso:.3f}')
print("------------------------------------------------")
print(f'o valor gasto de alcool é:{gastoalco:.3f}')
media = div / 30
media2 = div2 / 30 
print("------------------------------------------------")
print(f'a media gasta mensalmente de gasolina é: {media:.3f}')
print("------------------------------------------------")
print(f'a media gasta mensalmente de alcool é: {media2:3f}')
print("------------------------------------------------")