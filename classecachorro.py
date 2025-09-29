class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
#Correto: Cria um objeto da classe 'Cachorro' usando parênteses
meu_cachorro = Cachorro ("Max", 2)

print(f"Meu cachorro se chama {meu_cachorro.nome}") 
print(f"e tem {meu_cachorro.idade} anos.")

#Observações Importantes:
#self em self.nome serve para indicar que a variável nome pertence 
# ao objeto específico que está sendo manipulado naquele momento.
# Em outras palavras, self é uma referência a própria instância da classe.