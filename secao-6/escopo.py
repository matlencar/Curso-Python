from time import process_time_ns


escopo_global = "Tchau"

def teste():
    teste = "Ola"
    print(teste)
    print(escopo_global)
    if numero == 10:
        print("Você ganhou !!!")
        
teste()

escopo_global = "Até logo"
numero = 12

teste()
    