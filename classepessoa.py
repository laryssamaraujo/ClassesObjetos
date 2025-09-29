class Pessoa:
    def __init__(self, nome, idade, altura, telefone):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.telefone = telefone
        
        
minha_pessoa = Pessoa ("Laryssa", 29, 1.76, 83996246019)

print(f"Eu me chamo {minha_pessoa.nome}, tenho {minha_pessoa.idade} anos, com {minha_pessoa.altura} de altura, e meu telefone é {minha_pessoa.telefone}.")