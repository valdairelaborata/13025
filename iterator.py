# Criando um objeto iterável (uma lista)
my_list = [1, 2, 3, 4, 5]

# Obtendo um iterador a partir do objeto iterável
my_iterator = iter(my_list)


# Iterando pelos elementos usando um loop while
try:

    while True:
        element = next(my_iterator)
        print(element)

except StopIteration:
    pass

