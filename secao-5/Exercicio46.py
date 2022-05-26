lista = [5, 7, 88, 93,13, 14,2]

menor_valor = lista[0]

for n in lista:
    if n < menor_valor:
        menor_valor = n

print(menor_valor)