salario = float(input("Qual é o seu salario atual? "))

porcentagem = float(input("A porcentagem é de aumento salarial: "))

aumento = salario + (salario * (porcentagem/100))




print("O salario do funcionario foi aumentado para R$%.2f " % aumento )