notas = [10, 7, 9, 6, 8]

i = 0
soma = 0

while i < 5:
    soma = soma + notas[i]
    i = i + 1
    
    media = soma / 5

print("O aluno teve media %.1f na materia " % media)