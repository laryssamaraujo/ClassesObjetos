class Animal:
    
    def __init__(self, nome, idade, alimentação):
        self.nome = nome
        self.idade = idade
        self.alimentação = alimentação
        
    def exibirDetalhes (self):
            return f"Nome: '{self.nome}' | Idade: {self.idade}"
    def exibirAlimento (self):
            return f"Alimentação:'{self.alimentação}'"
        
animal1 = Animal("Gato", "2 anos", "Ração e leite")
animal2 = Animal("Leão", "5 anos", "Carne")
animal3 = Animal("Vaca", "10 anos", "Palma e campim")

print("-- Animais Pesquisados --")
print(animal1.exibirDetalhes())
print(animal1.exibirAlimento())

print(animal2.exibirDetalhes())
print(animal2.exibirAlimento())

print(animal3.exibirDetalhes())
print(animal3.exibirAlimento())