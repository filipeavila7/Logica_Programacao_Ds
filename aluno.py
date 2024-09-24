alunos = {}
while True:
    print()
    print(30 * '=', 'MENU', 30 * '=' )
    print('1. cadastrar alunos e mostrar a media')
    print('2. listar alunos')
    print()
    opcao = input('digite uma opção:')

    if opcao == '1':
        matricula = input('digite a matricula do aluno que deseja cadastrar:')
        nm = input('digite o nome do aluno:')
        nt1 = float(input('digite a nota de portugues:'))
        nt2 = float(input('digite a nota de matematica:'))
        nt3 = float(input('digite a nota de python:'))

        media = (nt1 + nt2 + nt3) / 3
       

        alunos[matricula] = {'nome' : nm, 'portugues' : nt1, 'matematica' : nt2, 'python' : nt3, 'media':media}
        

    elif opcao == '2':
        for chave, dados in alunos.items():
            print(f'matricula: {chave}, nome: {dados['nome']}, portugues: {dados['portugues']}, matematica: {dados['matematica']}, python: {dados['python']}, media: {dados['media']:.2f}')
        

   
   



