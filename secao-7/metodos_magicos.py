class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def __str__(self):
        return "O nome do usuario %s e tem %d anos e é um %s" %(self.nome, self.idade, self.profissao)
    
    
matheus = Pessoa("Matheus", 27, "Programador")

print(matheus.__str__())