import random
import os

class Personagem():
    def __init__(self, nome, vida, defesa, stamina, estus = 5):
        self.__nome = nome
        self.__vida = vida
        self.__defesa = defesa
        self.__stamina = stamina
        self.__estus = estus

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, defesa):
        self.__defesa = defesa



    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, stamina):
        self.__stamina = stamina


    @property
    def estus(self):
        return self.__estus

    @estus.setter
    def estus(self, estus):
        self.__estus = estus





    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 10
        self.stamina -= 5
        print(f'o {self.nome} atacou o {personagem.nome} e o {personagem.nome} ficou com {personagem.vida} pontos de vida')

    def curar(self):
        self.vida += 10
        self.stamina += 10
        self.estus -= 1
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual: {self.vida}')

    def especial(self, personagem):
        personagem.vida -= 10
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial no {personagem.nome}')

     


class Cavaleiro(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 20
        self.stamina -= 5
        print(f'{self.nome} desferiu um golpe forte de espada em {personagem.nome}')

    def curar(self):
        self.vida += 10
        self.stamina += 10
        self.estus -= 1
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida.')

    def especial(self, personagem):
        personagem.vida -= 25
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial em {personagem.nome}')

    


class Mago(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 15
        self.stamina -= 5
        print(f'{self.nome} desferiu uma magia potente em {personagem.nome}.')

    def curar(self):
        self.vida += 10
        self.stamina += 10
        self.estus -= 1
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida.')

    def especial(self, personagem):
        personagem.vida -= 29
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial em {personagem.nome}')


class Demonio(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 25
        self.stamina -= 5
        print(f'{self.nome} deferiu um feitiço maligno em {personagem.nome}. ')
    def curar(self):
        self.vida += 10
        self.estus -= 1
        self.stamina += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida.')

    def especial(self, personagem):
        personagem.vida -= 30
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial em {personagem.nome}')


class Golem(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 23
        self.stamina -= 5
        print(f'{self.nome} deferiu um ataque de força bruta em {personagem.nome}.')

    def curar(self):
        self.vida += 10
        self.estus -= 1
        self.stamina += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida.')

    def especial(self, personagem):
        personagem.vida -= 40
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial em {personagem.nome}')


class Arqueiro(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 18
        self.stamina -= 5
        print(f'{self.nome} atirou uma flecha poderosa em {personagem.nome}.')

    def curar(self):
        self.vida += 10
        self.estus -= 1
        self.stamina += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida.')
    def especial(self, personagem):
        personagem.vida -= 25
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial em {personagem.nome}')


class Samurai(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 18
        self.stamina -= 5
        print(f'{self.nome} desferiu um golpe de katana poderoso no {personagem.nome}.')
    def curar(self):
        self.vida += 10
        self.estus -= 1
        self.stamina += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida.')

    def especial(self, personagem):
        personagem.vida -= 35
        self.stamina -= 10
        print(f'PODER MÁXIMOOOO!! {self.nome} usou um golpe especial em {personagem.nome}')


# Criação dos personagens
samurai = Samurai('Shipin', 135, 14, 50)
cavaleiro = Cavaleiro('Artorias', 130, 10, 35)
cavaleiro2 = Cavaleiro('Soul of Cinder', 125, 8, 45)
demonio = Demonio('Bapihormet', 100, 15, 30)
golem = Golem('Rocker', 150, 13, 60)
mago = Mago('Sulivanh', 95, 15, 30)
mago2 = Mago('Gwendolyn', 90, 10, 28)
arqueiro = Arqueiro('Igon', 100, 12, 34)
mago3 = Mago('Mary', 120, 9, 30 )


def escolher_bonecos():
    bonecos = [samurai, cavaleiro, cavaleiro2, demonio, golem, mago, mago2, mago3, arqueiro]
    print('esolha seu personagem com o numero correspondente:')
    for i, personagem in enumerate(bonecos):
        print(f'{i + 1}. Nome: {personagem.nome} -- Vida: {personagem.vida} -- Stamina: {personagem.stamina} -- Frascos: {personagem.estus}')


    escolha_player = int(input('Escolha um personagem:')) -1
    player = bonecos[escolha_player]

    bonecos_adversario = [personagem for i, personagem in enumerate(bonecos) if i != escolha_player]
    adversario = random.choice(bonecos_adversario)

    print(f'voce escolheu o {player.nome}, seu adversário é {adversario.nome}')

    return player, adversario


def jogo():
    player, adversario = escolher_bonecos()


    while player.vida > 0 and adversario.vida > 0:
        

        print(f' Nome: {player.nome} -- Vida: {player.vida} -- Stamina: {player.stamina} -- Frascos: {player.estus}')
        print(f' Adversário: {adversario.nome} -- Vida: {adversario.vida} -- Stamina: {adversario.stamina} -- Frascos: {adversario.estus}')
        

        print('digite 1. para atacar')
        print('digite 2. para se curar')
        print('digite 3. para especial')
        print('digite 4. para desistir/fugir')



        opcao = int(input('digite alguma coisa:'))
        os.system('cls')

        if opcao == 1:
            if player.stamina >= 5:
                player.atacar(adversario)
            else:
                 print(f'a stamina de {player.nome} acabou')

        elif opcao == 2:
            if player.estus > 0:
                player.curar()
            else:
                print(f'os frascos de {player.nome} acabaram!')

        elif opcao == 3:
            if player.stamina >= 10:
                player.especial(adversario)
            else:
                print(f'a stamina de {player.nome} acabou')

        elif opcao == 4:
            print(f'o cagão do {player.nome} fugiu ou desistiu da luta kkkk, fim de jogo')
            break

        else:
            print('digite alguma opção válida animal!')



        if adversario.vida > 0:
            opcao_adversario = random.choice([1,2,3])
            if opcao_adversario == 1:
                if adversario.stamina >= 5:
                    adversario.atacar(player)
                else:
                    print(f'{adversario.nome} não tem stamina')
           
            elif opcao_adversario == 2:
                if adversario.estus > 0:
                    adversario.curar()
                else:
                    print(f'os frascos do {adversario.nome} acabaram!')
            else:
                if adversario.stamina >= 10:
                    adversario.especial(player)
                else:
                    print(f'{adversario.nome} não tem stamina')


        if player.vida <= 0:
            print(f' {player.nome} morreu, fim de jogo!')
            break

        elif adversario.vida <= 0:
            print(f'{adversario.nome} morreu, fim de jogo!')
            break

jogo()
        




        
    
       


    