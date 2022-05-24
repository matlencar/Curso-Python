idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode entrar na balada.")
    
    metodo_pagamento = input("Como vai pagar a entrada da balada?")
    
    if metodo_pagamento == "dinheiro":
        print("A fila do dinheiro é a numero 1")
    else:
        print("A fila de cartão é a numero 2")
else:
    print("Você não pode entrar na balada")