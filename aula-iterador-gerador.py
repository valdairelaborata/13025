# # Criando um objeto iterável (uma lista)
# my_list = [1, 2, 3, 4, 5] #"Linhas de uma tabela/documento"

# # Obtendo um iterador a partir do objeto iterável
# my_iterator = iter(my_list)

# # Iterando pelos elementos usando um loop while
# try:
#     while True:
#         element = next(my_iterator)
#         print(element)
# except StopIteration:
#     pass



def contador(max_value):
    count = 1
    while count <= max_value:        
        yield count
        count += 1

# Criando um objeto gerador
gen = contador(5)

# Usando o gerador para obter os valores
print(next(gen))  # Saída: 1
print(next(gen))  # Saída: 2
print(next(gen))  # Saída: 3
print(next(gen))  # Saída: 4
print("Outra coisa!!!!!")
print(next(gen))  # Saída: 5





# # Expressão geradora para criar um gerador de números pares
# even_numbers = (x for x in range(1, 11) if x % 2 == 0)

# # Usando um loop for para iterar pelos números pares
# for num in even_numbers:
#     print(num)





