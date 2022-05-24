salario = float(input("Digite seu salario: "))

imposto_de_renda = 1800.00

if(salario > imposto_de_renda):
    print("Sera necessario pagar imposto de renda, pois seu salario é %.2f" % salario)
else:
    print("Não precisa pagar o IR, pois seu salario é %.2f" % salario)