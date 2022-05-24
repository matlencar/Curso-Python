poupanca = 200
saque = 300

if saque <= poupanca:
    print("Você sacou R$%d reais" % saque)
else:
    print("Você não tem saldo para sacar R$%d" % saque)
    print("sua poupança tem no momento R$%d" % poupanca)