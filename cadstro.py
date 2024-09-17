lista_usuario = []
while True:
    print()
    print(30 * '=', 'MENU', 30 * '=' )
    print('1. cadastrar usuário')
    print('2. listar usuário')
    print('3. mostrar a lista:')
    print("4. sair:")
    print('5. excluir usuario:')
    print('6. buscar pelo nome:')
    print('7. inserir em uma posição:')
    print(64 * '=')
    print()
    
    opcao = input('digite a opcao desejada: ')
    #add usuario:
    if opcao =='1':
        nm = input('digite um nome que deseja cadastrar:').lower()
        
        if nm != '':
            lista_usuario.append(nm)
            print(f'usuario {nm} cadstrado')
        else:
            print('digite um valor:')
    #listar usuario:
    elif opcao =='2':
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}° {n}')
       
    #sair do sistema
    elif opcao == '4':
        print('saindo do sistema:')
        break
    
    elif opcao == '3':
        print(lista_usuario)
        '''
    elif opcao == '5':
        nm = input('digite o nome que deseja excluir:').lower()
        
       
        for i in lista_usuario:
            lista_usuario.remove(i)
            print('usuário removido')
        '''
    # excluir
    elif opcao == '5':
        for i, n in enumerate(lista_usuario):
            print(f'{i}° {n}')

        posicao = int(input('digitr o numero do usuario que deseja excluir:'))
        
        for j, _ in enumerate(lista_usuario):
            if j == posicao:
                lista_usuario.pop(j)
                print(f'usuario da posicao {j} foi removido')
    #buscar 
    elif opcao == '6':
        buscar = input('digite o nome que deseja buscar:')
        
        if buscar != '':
            for i in lista_usuario:
                if i == buscar:
                    print(i)
    
    #inserir na posicao
    elif opcao == '7':
        nvnm = input('digite o nome que deseja inserir:').lower()
        posi = int(input('digite a posição que deseja inserir: '))
        posi -=1
        if posi >= 0 and posi <= len(lista_usuario):
            lista_usuario.insert(posi, nvnm)
        else:
            print('posicao invalida')

    else:
        print('digite um numero valido')
                   
    

        
                

    

   

  
  


