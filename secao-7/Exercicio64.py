class Mamifero:
    def __init__(self, patas, orelhas):
        self.patas = patas
        self.orelhas = orelhas
    
    def andar(self):
        print("O mamifero andou")
        
class Cachorro(Mamifero):
    def __init__(self, patas, orelhas,cor_do_pelo):
        super().__init__(patas, orelhas)
        self.cor_do_pelo = cor_do_pelo
    
    def latir(self):
        print("Au au")

turca = Cachorro(4, 2, "caralemo")

turca.andar()
turca.latir()

class Gato(Mamifero):
    def __init__(self, patas, orelhas,listras):
        super().__init__(patas, orelhas)
        self.listras = listras
        
    def miar(self):
        print("Miauuu")
        
clebson = Gato(4,2,False)

clebson.andar()
clebson.miar()

print(clebson.listras)