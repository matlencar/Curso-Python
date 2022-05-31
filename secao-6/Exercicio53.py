def listaPar(l):
    novaLista = []
    
    for numero in l:
        if numero % 2 == 0:
            novaLista.append(numero)
            
    return novaLista

lista = [1,2,3,4,5,6,7,8]

listaPar = listaPar(lista)

print(listaPar)

lista2 = [1,2,3,4,5,6,7,877,91,13,12,14,16,22,28,34,42,43]

print(listaPar(lista2))