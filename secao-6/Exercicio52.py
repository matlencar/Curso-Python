def checa_tamanho_texto(texto):
    
    resposta = ""

    if len(texto) >= 20:
        resposta = "Texto muito longo"
    else:
        resposta = "Texto curto"

    return resposta


texto_um = "Matheus é programador"

resp_um = checa_tamanho_texto(texto_um)

print(resp_um)

print(len(resp_um))
print(checa_tamanho_texto)