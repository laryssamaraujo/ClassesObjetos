class Cadastro:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
    def exibirInfor (self):
            return f"Nome: '{self.nome}' | Email: {self.email}"
    def exibirSenha (self):
            return f"Senha:'{self.senha}'"
        
cadastro1 = Cadastro("Laryssa", "laryssam444@gmail.com", "22011996")
cadastro2 = Cadastro("Isaac", "issacsmsbn@gmail.com", "250215")

print("-- Cadastros Efetuados --")
print(cadastro1.exibirInfor())
print(cadastro1.exibirSenha())

print(cadastro2.exibirInfor())
print(cadastro2.exibirSenha())