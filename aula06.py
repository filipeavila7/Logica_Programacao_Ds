lista = [1,32,31,65,3,2,43,23,22,12]
print(lista[0])
print(lista[0:5])
lista.sort()
lista.sort(reverse=True)
print(f'lista ordena {lista}')

lista.remove(22)
lista.pop(5)
del lista[2:5]

nome = 'shipin'
lista.append(nome)
print(lista)

# inserção
lista.insert(2, 'patock')
print(lista)

# substituição
lista[2] = 'shipadas'
print(lista)

print('patock' not in lista)
print(lista)

print('patock' in lista)
print(lista)

'''
if condicao:
    resultado
    
else:
    resultado
'''

'''
if condicao:
    resultado
no mesmo nivel q o if
'''

'''
if condicao:
    if condicao:
        if condicao:
            if condição'''


'''
if condicao:
    pass
else:
    if condicao:
        pass
    else:
        if condicao:
            pass
        else
            if condição
            '''

if 'shipin' in lista:
    # so sera executado quando a condicao for true
    print('sim ele esta na lista')
else: # so sera executado quando a condicao for false
    print('ele nao esta na lista')


notas = []
nt1 = int(input('digite a nota de mat:'))
notas.append(nt1)
nt2 = int(input('digite a nota de port:'))
notas.append(nt2) 
qntnt = len(notas) # conta a qntdade de vlores q tem na lista
print(qntnt)
soma = sum(notas) #soma os valores 
media = soma / qntnt
print(20*'-','boletim escolar',20*'-')
print(f'*a media das notas é:{media}*')
if media >= 7:
    print('*-*aprovado*-*')
elif media >=5:
    print('*-*recuperação*-*')
else:
    print('*-*reprovado*-*')