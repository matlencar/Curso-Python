numero = int(input("Digite um numero: "))
num_x = 10
num_y = 20

if numero > num_x:
    
    if numero > num_y:
        print("Sua multiplicação por 2 é: ",numero * 2)
    else:
        print("Sua multiplicação por 5 é:", numero * 5)
else:
    print("O numero precisa ser maior do que 10")