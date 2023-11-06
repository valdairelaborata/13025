def gerador_pares():    
    numero = 2
    while True:
        yield numero
        numero += 2

    
gen = gerador_pares()

for _ in range(5000):
    print(next(gen))
