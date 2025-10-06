class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.lido = False
        
        
    def marcar_como_lido(self):
        self.lido = True
        print(f" - Status alterado: '{self.titulo}' agora está marcado como lido.")
    
    def exibir_status(self):
        status = "lido" if self.lido else "pendente"
        print(f"O livro '{self.titulo}', de {self.autor} está {status}.")
    
livro1 = Livro("Café com Deus Pai", "Júnior Rostirola")
livro2 = Livro("Você é Insubstituível", "Augusto Cury")

print(" - Status de Livros - ")
print(livro1.marcar_como_lido())
print(livro2.exibir_status())