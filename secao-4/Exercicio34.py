num = int(input("Digite um numero: "))

divisoes = 0
contador = num

while contador > 0:
    
    if num % contador == 0:
        divisoes = divisoes + 1
    
    contador = contador - 1
    
if divisoes == 2:
    print("O numero %d é par" % num)
else:
    print("O numero %d não é primo: " % num)