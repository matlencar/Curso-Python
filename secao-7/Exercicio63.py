class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print("Ola galera")
        
class Superheroi(Pessoa):
        def __init__(self, nome, idade, super_poder):
             super().__init__(nome, idade)
             self.super_poder = super_poder
             
        def utilizar_super_poder(self):
            print("O heroi utilizou o(a) %s" % self.super_poder)
        
        

joao = Pessoa("Joao", 21)

joao.falar()

matheus = Superheroi("Matheus", 29, "Super-Força")

matheus.falar()

matheus.utilizar_super_poder()