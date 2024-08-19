# Atividade 02

## Exemplos
Os métodos, as funções de uma classe, podem acessar e alterar valores dos atributos do objeto.

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

# Perguta ao usuário quantos anos a mais adicionar
anos1 = int(input(f"Quantos anos a mais {pessoa3.nome} tem? "))

# Adiciona a quantidade de anos digitada pelo usuário
pessoa3.adicionar_idade(anos1)

```

## Questões

**Instruções**: Crie um arquivo chamado `produto.py` e faça as seguintes questões.

1. Crie uma classe `Produto` com os atributos nome, descrição, preço e estoque. Defina preço como `float`, estoque como `int`, os demais atributos como `string`.

2. Defina esses atributos no construtor da classe.

3. Crie o método `mostrar_informações` para a classe, esse método deve imprimir os atributos do produto.

4. Crie o método `vender` para a classe, esse método deve receber a varíavel `quantidade`. Se a quantidade vendida for maior que o estoque, deve imprimir uma mensagem de erro. Caso contrário, deve atualizar o estoque subtraindo a quantidade vendida.

5. Crie o método `atualizar_preco`, esse método deve receber a varíavel `novo_preco` e atualizar o preço do produto. Se o novo preço for menor que 0, deve imprimir uma mensagem de erro.

6. Crie um objeto da classe Produto e defina seus atributos. Faça a chamada dos métodos desse objeto.
