class Pessoa:
    def falar(self):
        print("Ola pessoal ")
        
class Matheus(Pessoa):
    def falar(self):
        print("Ola pessoal, eu sou o matheus")


matheus = Matheus()

matheus.falar()