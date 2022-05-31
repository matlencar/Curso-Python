def reune_dados(nome,idade,profissao,fnct):
    apresentacao = fnct(nome,idade,profissao)
    return apresentacao

def apresenta_dados(nome,idade,profissao):
    frase =  "O nome do usuario é %s e sua idade é de %d anos e ele é um %s" %(nome,idade,profissao)
    return frase

print(reune_dados("Matheus alencar",27,"Dev Jr",apresenta_dados))

apresentacao = reune_dados("Matheus alencar",27,"Dev Jr",apresenta_dados)

print(apresentacao)

