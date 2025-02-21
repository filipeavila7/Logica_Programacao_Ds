class Personagem():  # Define uma classe chamada Personagem.
    # Construtor para inicializar os atributos nome e vida do personagem.
    def __init__(self, nome, vida):  # Método construtor (__init__) para inicializar os atributos de cada personagem.
        self.__nome = nome  # Atribui o valor passado como 'nome' ao atributo privado __nome (encapsulamento).
        self.__vida = vida  # Atribui o valor passado como 'vida' ao atributo privado __vida (encapsulamento).

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

    def atacar(self, personagem):  # Método para atacar outro personagem.
        personagem.vida -= 10  # Diminui a vida do personagem alvo em 10 pontos.
        print(f'{self.nome} atacou {personagem.nome}')  # Exibe uma mensagem informando sobre o ataque.

# Definindo classes que herdam da classe Personagem, com diferentes tipos de ataque.
class Cavaleiro(Personagem):  # A classe Cavaleiro herda de Personagem.
    def atacar(self, personagem):  # Redefine o método 'atacar' para Cavaleiro.
        personagem.vida -= 15  # Diminui a vida do personagem alvo em 15 pontos (dano maior que o padrão).
        print(f'{self.nome} deferiu um golpe de espada no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')  # Exibe a mensagem com dano e nova vida.

class Mago(Personagem):  # A classe Mago herda de Personagem.
    def atacar(self, personagem):  # Redefine o método 'atacar' para Mago.
        personagem.vida -= 12  # Diminui a vida do personagem alvo em 12 pontos.
        print(f'{self.nome} deferiu um feitiço pesado contra o {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')  # Exibe a mensagem com dano e nova vida.

class Arqueiro(Personagem):  # A classe Arqueiro herda de Personagem.
    def atacar(self, personagem):  # Redefine o método 'atacar' para Arqueiro.
        personagem.vida -= 14  # Diminui a vida do personagem alvo em 14 pontos.
        print(f'{self.nome} atirou uma flecha poderosa no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')  # Exibe a mensagem com dano e nova vida.

class Demonio(Personagem):  # A classe Demonio herda de Personagem.
    def atacar(self, personagem):  # Redefine o método 'atacar' para Demonio.
        personagem.vida -= 35  # Diminui a vida do personagem alvo em 35 pontos (dano muito maior).
        print(f'{self.nome} deferiu um feitiço maligno no {personagem.nome}. {personagem.nome} agora possui: {personagem.vida} pontos de vida')  # Exibe a mensagem com dano e nova vida.

# Criando instâncias dos personagens com seus nomes e pontos de vida.
cavaleiro = Cavaleiro('Artorias', 125)  # Cria um personagem Cavaleiro com nome e vida.
cavaleiro1 = Cavaleiro('Soul of Cinder', 130)  # Cria outro personagem Cavaleiro com nome e vida.
mago = Mago('Sulivanh', 95)  # Cria um personagem Mago com nome e vida.
mago1 = Mago('Gwendolyn', 90)  # Cria outro personagem Mago com nome e vida.
arqueiro = Arqueiro('Igon', 100)  # Cria um personagem Arqueiro com nome e vida.
demonio = Demonio('Bapihormet', 200)  # Cria um personagem Demonio com nome e vida.

# Exibindo as informações iniciais de nome e vida dos personagens.
print(f'Cavaleiro: {cavaleiro.nome} | Vida: {cavaleiro.vida}')  # Mostra o nome e a vida do Cavaleiro.
print(f'Mago: {mago.nome} | Vida: {mago.vida}')  # Mostra o nome e a vida do Mago.
print(f'Arqueiro: {arqueiro.nome} | Vida: {arqueiro.vida}')  # Mostra o nome e a vida do Arqueiro.

# Realizando ataques entre os personagens.
cavaleiro.atacar(cavaleiro1)  # O Cavaleiro 'Artorias' ataca o Cavaleiro 'Soul of Cinder'.
demonio.atacar(cavaleiro)  # O Demonio 'Bapihormet' ataca o Cavaleiro 'Artorias'.

# O print de cada ataque ocorre dentro dos métodos 'atacar' de cada classe. Ao atacar, o personagem perde pontos de vida e isso é mostrado na tela.
