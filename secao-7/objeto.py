class Pessoa:
    def __init__(self,nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
matheus = Pessoa("Matheus", 27,"Desenvolvedor")

print(matheus)

print(matheus.nome)
print(matheus.idade)
print(matheus.profissao)

if matheus.nome == "Matheus":
    print("nome é Matheus")