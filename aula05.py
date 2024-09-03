lista = ['shipin','patock','k']
print(lista)

lista2 = [1,2,3,4,5,6,7,8]
print(lista2[-1])

lista_int =[17,43,21,3,2,11,23,56,7]
print(f'direto no print: {sorted(lista_int)}') #organizar dentro do print
print(f'direto no print: {sorted(lista_int, reverse=True)}') #inverter dentro do print
lista_int.sort() #imprimir a lista organizada crescente
print(lista_int)
lista_int.sort(reverse=True) #decrescente
print(lista_int)

# remove , pop , del

listnm = ['shipadas','patock','shipin','otario','jean','shipin']
print(listnm)
listnm.remove('shipin')   #remove apenas o primeiro shipin q ele encontrar
print(listnm)

listnm.pop(-2)   # remove pelo indice 
print(listnm)

del listnm[:4] #remover de um a outro
print(listnm)

nomes = []                                  #inserir nome na lista 
nvnome = input('digite um novo nome:')
nomes.append(nvnome)
print(nomes)
