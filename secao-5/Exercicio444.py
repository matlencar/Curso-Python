lista = [10,20,30,40,50]

num_encontrado = int(input("Qual numero deseja buscar? "))

encontrado = False


for n in lista:
    if n == num_encontrado:
        print("O numero %d foi encontrado " % num_encontrado)
        encontrado = True
        
if encontrado == False:
    print("Não encontramos o numero %d" % num_encontrado)