class Pessoa:
    # Atributos da Classe Pessoa
    nome = ""
    idade = 0
    altura = 0.0

    # O construtor recebe os atributos
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # Métodos define ações do objeto
    def andar(self):
        print(f"{self.nome} está andando...")

# Criando um objeto da classe
pessoa1 = Pessoa("Ana", 18, 1.75)
# Também podemos criar um objetos dessa forma
pessoa2 = Pessoa(nome="Julio", idade=19, altura=1.80)

# Depois de criar um objeto podemos chamar os métodos da classe dele
pessoa1.andar()
# Ou exibir seus atributos
print(f"Nome: {pessoa2.nome}. Idade: {pessoa2.idade}")
