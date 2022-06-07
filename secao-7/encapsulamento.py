class Aviao:
    _asas = 2
    
    def __init__(self,marca):
        self.marca = marca
        
    def mostrar_asas(self):
        print("O aviao tem %d asas" % self._asas)
        
aviao = Aviao("Aviões da hora de codar")

print(aviao.marca)

aviao.mostrar_asas()