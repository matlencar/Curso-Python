conta_bancaria = 359.56

deposito = float(input("Digite uma nova quantia de dinheiro: "))

saldo = conta_bancaria + deposito

fatura_cartao = saldo - 125.98

print("O meu saldo na minha conta é de R$ %.2f" % deposito, "reais")
print("O valor do meu saldo depois que pague minha fatura foi de R$ %.2f" % fatura_cartao, "reais")