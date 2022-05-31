import random

aleatorio = random.randint(1,10)

palpite = int(input("Advinhe um numero: "))

if aleatorio == palpite:
    print("Parabens você acertou  o numero é: %d" % aleatorio)
else:
    print("Você errou o numero era: %d" % aleatorio)