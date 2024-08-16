# Atividade 02

## Exemplos
Os métodos, as funções de uma classe, podem acessar alterar valores dos atributos do objeto.

**[pessoa.py](../exemplos/pessoa.py)**
```python
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

    # Métodos podem alterar os valores dos atributos da classe
    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} completou {self.idade} anos!")

    # Métodos podem receber variaveis de fora da classe
    def adicionar_idade(self, anos):
        self.idade = self.idade + anos
        print(f"{self.nome} tem {anos} a mais! Agora tem {self.idade}")
```

- Método `fazer_aniversario`:
Este método adiciona mais 1 no atributo idade do objeto e imprime uma mensagem informando quantos anos completou.

- Método `adicionar_idade`:
Este método adiciona um número específico no atributo idade do objeto e imprime uma mensagem informando os anos.

```python
pessoa3 = Pessoa(nome="Pedro", idade=16, altura=1.60)
# Mostra a idade inicial
print(f"{pessoa3.nome} tem {pessoa3.idade} anos.")

# Chama o método para fazer aniversário
pessoa3.fazer_aniversario()  # idade = 17

# Pede ao usuário quantos anos a mais adicionar
anos1 = int(input(f"Quantos anos a mais {pessoa3.nome} tem? "))

# Adiciona a quantidade de anos fornecida pelo usuário
pessoa3.adicionar_idade(anos1)

```

## Questões

1.

