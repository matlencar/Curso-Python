produto_a = ["Camisa","Azul", 26.90]
produto_b = ["Bermuda","Marrom", 112.20]
produto_c = ["Jaqueta","Preta", 200.00]

lista_produtos = [produto_a, produto_b,produto_c]

print(lista_produtos)

for produto in lista_produtos:
    print("O produto é: %s e tem a cot %s e o seu preço é: R$%.2f " % (produto[0], produto[1],produto[2]))