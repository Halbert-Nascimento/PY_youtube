"""
OBJETO e uma instância da classe, onde pode se criado vários objetos diferentes a partir de uma classe, quando se instancia um objeto ele recebe todos os atributos e métodos dessa classe em específico que podem ser alterados individualmente para cada objeto.


Uma classe serve como uma espécie de modelo que define as características e comportamentos que um objeto pode ter . Ela ajuda a organizar o código de forma eficiente, permitindo a criação de múltiplos objetos que compartilham essas características e comportamentos. 
Esses objetos de classe podem representar entidades do mundo real ou simplesmente serem estruturas de dados abstratas. Em resumo, as classes são a base da programação orientada a objetos e promovem a reutilização de código, tornando-o mais organizado e modular.


os ATRIBUTOS de uma classe são as características, estado ou propriedades que o objeto pode ter, e essas informações podem ser armazenadas em variáveis.

já os METODOS são funções dentro da classe que podem ser chamadas para executar ações, comportamentos ou operações.


SUB-CLASSES as sub-class recebem a classe pai como parâmetro onde ela herda seu atributos e métodos e ainda pode ter seus próprios atributos e métodos e modificar os atributos herdados
"""

class Animal:
    def __init__(self, nome, altura, peso): 
        #__init__ é um método especial usado para inicializar os atributos de um objeto quando  ele é criado a partir de uma classe. Ele é executado automaticamente quando um objeto é instanciado.
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def info(self): # Metodo usado para fornecer uma representação de string legível.
        
        print("\nAtributos:")
        return f"Nome: {self.nome} \nAltura: {self.altura:.2f} \nPeso: {self.peso:.2f} KG"

class dog(Animal):
    def som(self):#metodo som
        return "Latido: Au au"

cachorro_1 = Animal("Gamora", 20, 8)
cachorro_1.altura = 23
cachorro_1.peso = 12
print(cachorro_1.info())

cachorro_2 = dog("Bily", 15.5, 8)
print(cachorro_2.info())
print(cachorro_2.som())
cachorro_2.altura = 10
cachorro_2.peso = 2
print(cachorro_2.info())