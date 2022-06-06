class Carro:
    def __init__(self, portas, motor, teto_solar,marca,preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco
        
        
polo = Carro(4,1.4,False, "VW",50000)

print(polo.marca)
print(polo.preco)
        