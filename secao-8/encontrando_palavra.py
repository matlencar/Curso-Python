frase = "Eu quero encontrar o peixe"

print(frase.find("peixe"))

if frase.find("peixe") > 0:
    print("Encontrei o peixe")
    
print(frase.find("tubarao"))

if frase.find("tubarao") ==-1:
    print("Não há tubarao na frase")
else:
    print("há tubarao")