def gerador_pares():
    numero = 2
    while True:
        yield numero
        numero += 2

gerador = gerador_pares()


# Imprimir os primeiros 10 números pares gerados
for _ in range(10):
    print(next(gerador))





