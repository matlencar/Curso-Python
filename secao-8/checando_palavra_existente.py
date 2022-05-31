frase = "esta é a frase que queremos achar uma palavra"

print(frase)

if "frase2" in frase:
    print("Encontramos a palavra frase")
    
print("frase2" in frase)

if "segunda-feira" not in frase:
    print("Não encontramos a segunda-feira")
    
print("segunda-feira" not in frase)