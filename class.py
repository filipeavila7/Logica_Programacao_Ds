class Personagem():  # Define uma classe chamada Personagem.
    #construtor - para qnd eu criar um objeto, ele acessa os atributos da classe
    def __init__(self, nome, vida):  # Método construtor (__init__) para inicializar os atributos de cada personagem.
        self.__nome = nome  # Atribui o valor passado como 'nome' ao atributo privado __nome? encapsulamento
        self.__vida = vida  # Atribui o valor passado como 'vida' ao atributo privado __vida. 

    @property
    def nome(self):  # Define um método getter para o atributo 'nome'.
        return self.__nome  # Retorna o valor do atributo privado '__nome'.
    
    @nome.setter
    def nome(self, nome):  # Define um método setter para o atributo 'nome'.
        self.__nome = nome  # Define o valor do atributo privado '__nome' como o valor passado no parâmetro 'nome'.

    @property
    def vida(self):  # Define um método getter para o atributo 'vida'.
        return self.__vida  # Retorna o valor do atributo privado '__vida'.

    @vida.setter
    def vida(self, vida):  # Define um método setter para o atributo 'vida'.
        self.__vida = vida  # Define o valor do atributo privado '__vida' como o valor passado no parâmetro 'vida'.



    def atacar(self, personagem):
        personagem.vida -= 10
        print(f'{self.nome} atacou {personagem.nome}')



class Cavaleiro(Personagem):
    def atacar(self, personagem):
        personagem.vida -= 15
        print(f'{self.nome} deferiu um golpe de espada no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida' )



class Mago(Personagem):
    def atacar(self, personagem):
        personagem.vida -= 12 
        print(f'{self.nome} deferiu uma feitiÇo pesado contra o {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida' )


class Arqueiro(Personagem):
    def atacar(self, personagem):
        personagem.vida -= 14
        print(f'{self.nome} atirou uma flecha poderosa no {personagem.nome} . {personagem.nome} agora possui: {personagem.vida} pontos de vida')

class Demonio (Personagem):
    def atacar(self, personagem):
        personagem.vida -= 35
        print(f'{self.nome} deferiu um feitiço maligno no {personagem.nome} . {personagem.nome} agora possui: {personagem.vida} pontos de vida')
        
        


cavaleiro = Cavaleiro('Artorias', 125)
cavaleiro1 = Cavaleiro('Soul of Cinder', 130)
mago = Mago('Sulivanh', 95)
mago1 = Mago('Gwendolyn', 90)
arqueiro = Arqueiro('Igon', 100)
demonio = Demonio('Bapihormet', 200)


print(f'Cavaleiro:{cavaleiro.nome} | Vida:{cavaleiro.vida}')
print(f'Mago:{mago.nome} | Vida:{mago.vida}')
print(f'Arqueiro:{arqueiro.nome} | Vida:{arqueiro.vida}')


cavaleiro.atacar(cavaleiro1)
demonio.atacar(cavaleiro)