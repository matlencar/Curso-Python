numero_1 = int(input("Digite um numero: "))

numero_2 = int(input("Digite um outro numero: "))

multiplicacao = numero_1 * numero_2

if multiplicacao <= 100:
    print("O numero é baixo %d" % multiplicacao)
else:
    print("O numero é alto %d " % multiplicacao)