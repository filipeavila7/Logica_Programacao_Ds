estoque = []
while True:
    print()
    print(30 * '=', 'MENU LOJA', 30 * '=' )
    print('1. adcionar produtos')
    print('2. atualizar quantidade de produtos')
    print('3. listar produtos disponíveis')
    print('4. calcular valor total em estoque')
    print('5. sair')

    opcao = input('digite uma opção:')

    if opcao == '1':
        nome = input('digite o nome do produto:')
        quantidade = int(input('digite a quantidade:'))
        preco = float(input('digite o preço:'))
        estoque.append([nome, quantidade, preco])

    
    
    elif opcao == '2':
        nome = input('digite o nome do produto que deseja atuallizar')
        nvqnt = int(input('digite a nova quantidade:'))
        encontrado = False 
        for produto in estoque:
            if produto[0] == nome:
                produto[1] == nvqnt
                print(f'quantidade do produto {nome} atualizada para {nvqnt}')
                encontrado = True 
                break
        if not encontrado:
            print(f'o produto {nome} nao foi encontrado')
    
    elif opcao == '3':
        if len(estoque) == 0:
            print('o estoque esta vazio')
        else:
            print('produtos no inventario:')
            for produto in estoque:
                print(f'nome: {produto[0]} | quantidade:{produto[1]} | valor:{produto[2]}')
   
    elif opcao == '4':
        valortt = 0
        for produto in estoque:
            valortt += produto[1] * produto[2]
        print(f'o valor total do estoque é: {valortt}')
    
    elif opcao == '5':
        break
       

    
       
    
      
   
