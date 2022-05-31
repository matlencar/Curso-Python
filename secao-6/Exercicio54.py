def cal_media(lista):
    media = 0
    soma = 0
    
    for n in lista:
        soma += n
        
    media = soma / len(lista)

    return media

notas = [9,5,7]

media_final = cal_media(notas)

print(media_final)
        
        