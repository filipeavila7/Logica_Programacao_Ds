usuario = {}
while True:
    print()
    print(30 * '=', 'MENU', 30 * '=' )
    print('1. cadastrar usuário')
    print('2. listar usuário')
    print('3. excluir usuario::')
    print("4. sair:")
    print(64 * '=')
    print()

    opcao = input('digite a opcao desejada: ')

    if opcao == '1':
       ide = input('digite o id do usuario que deseja cadastrar:')
       nm = input('digite um nome que deseja cadastrar:')
       cpf =  input('digite o cpf que deseja cadastrar:')
       idade =  input('digite a idade que deseja cadastrar:')
       usuario[ide] = {'nome': nm, 'CPF' : cpf, 'idade': idade}
       print(usuario)
    
        
       

        


    elif opcao == '2':
        for chave, dados in usuario.items():
            print(f'codigo: {chave}, nome: {dados['nome']}, cpf: {dados['CPF']}, idade: {dados['idade']}')
            
    elif opcao == '4':
       print('saindo...')
       break
            


    elif opcao == '3':
     remover = input('digite a chave que deseja remover:')
     if remover in usuario:
        del usuario[remover]
        print('usuario removido mano')
    else:
       print('esse usuario nao esta na lista')



       


    





   

        