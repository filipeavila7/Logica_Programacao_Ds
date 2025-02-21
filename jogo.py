class Personagem():
    def __init__(self, nome, vida, defesa):
        self.__nome = nome
        self.__vida = vida
        self.__defesa = defesa

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


    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 10 
        print(f' o {self} atacou o {personagem} e o {personagem} ficou com {personagem.vida} pontos de vida')



    def curar(self):
        self.vida + 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')


    def especial(self, personagem):
        personagem.vida -= 10
        




class Cavaleiro(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa
        personagem.vida -= 20
        print(f'{self.nome} desferiu um golpe forte de espada no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')
    def curar(self):
        self.vida += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')
    

class Mago(Personagem):
    def atacar(self, personagem):
        personagem.vida += personagem.defesa 
        personagem.vida -= 15
        print(f'{self.nome} desferiu uma magia potente no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')
    def curar(self):
        self.vida += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')
    

class Demonio(Personagem): 
    def atacar(self, personagem):  
        personagem.vida += personagem.defesa 
        personagem.vida -= 25  
        print(f'{self.nome} deferiu um feitiço maligno no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')
    def curar(self):
        self.vida += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')


class Golem(Personagem):
    def atacar(self, personagem):  
        personagem.vida += personagem.defesa 
        personagem.vida -= 23
        print(f'{self.nome} deferiu um ataque de força bruta no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')
    def curar(self):
        self.vida += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')

class Arqueiro(Personagem): 
    def atacar(self, personagem): 
        personagem.vida += personagem.defesa
        personagem.vida-= 18
        print(f'{self.nome} atirou uma flecha poderosa no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida') 
    def curar(self):
        self.vida += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')

class Samurai(Personagem): 
    def atacar(self, personagem): 
        personagem.vida += personagem.defesa
        personagem.vida -= 18
        print(f'{self.nome} desferiu um golpe de katana poderoso no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida') 
    def curar(self):
        self.vida += 10
        print(f'{self.nome} usou o frasco de estus e curou 10 pontos de vida. Vida atual:{self.vida}')




samurai = Samurai('Shipin',135, 14)
cavaleiro = Cavaleiro('Artorias', 130, 10)
cavaleiro2 = Cavaleiro('Soul of cinder', 125, 8)
demonio = Demonio('Bapihormet', 100, 15)
golem = Golem('Rocker', 150, 13)
mago = Mago('Sulivanh', 95, 15) 
mago2 = Mago('Gwendolyn', 90, 10)
arqueiro = Arqueiro('Igon', 100, 12)


    



samurai.atacar(cavaleiro)

samurai.curar()
    


