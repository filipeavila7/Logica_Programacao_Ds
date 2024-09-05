qnt = 0
soma = 0
for i in range(1,101):
    if i % 2 != 0:
        print(i)
        qnt +=1
        soma += i

print(f'a soma dos numeros impares é:{soma}')
print(f'a qntd de numeros impares é:{qnt}')

