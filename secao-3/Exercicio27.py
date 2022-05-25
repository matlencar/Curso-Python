renda_usuario = float(input("Informe sua renda para liberarmos um limite: "))

if renda_usuario < 2000.00:
    print("Podemos liberar um limite de R$1.000,00 reais")
elif renda_usuario < 4000.00:
    print("Podemos liberar um limite de R$2.000,00 reais")
elif renda_usuario < 10000.00:
    print("Podemos liberar um limite de R$3.000,00 reais")
elif renda_usuario >= 10000.00:
    print("Como sua renda ultrapassa os R$10.000 você precisa falar com o gerente")
else:
    print("Volte mais tarde para negociarmos com você !")