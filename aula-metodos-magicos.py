
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

#     def __del__(self):
#         print(f"{self.nome} está sendo destruído.")


# pessoa1 = Pessoa("João")


# pessoa2 = pessoa1  # Agora há duas referências para a mesma instância

# del pessoa1  # O objeto não é destruído porque ainda há uma referência a ele
# del pessoa2  # Agora o objeto é destruído, chamando __del__


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade


#     # def to_string(self):
#     #     return f"{self.nome}, {self.idade} anos"

#     def __str__(self):
#         return f"{self.nome}, {self.idade} anos"

# pessoa = Pessoa("João", 30)

# print(pessoa)  # Saída: João, 30 anos
# # print(pessoa.to_string())  # Saída: João, 30 anos


# class Pessoa():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def __repr__(self):
#         return f"Pessoa(nome='{self.nome}', idade={self.idade})"

# pessoa = Pessoa("Alice", 30)

# print(repr(pessoa))  # Saída: Pessoa(nome='Alice', idade=30)


# class Numero:
#     def __init__(self, valor):
#         self.valor = valor
    
#     def __add__(self, outro):
#         novo_valor = self.valor + outro.valor
#         return Numero(novo_valor)

# numero1 = Numero(5)
# numero2 = Numero(10)
# resultado = numero1 + numero2
# print(resultado.valor)  # Saída: 15



# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def __eq__(self, outra):
#         return self.nome == outra.nome and self.idade == outra.idade

# pessoa1 = Pessoa("Alice", 30)
# pessoa2 = Pessoa("Alice", 30)
# print(pessoa1 == pessoa2)  # Saída: True



# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def __ne__(self, outra):
#         return not self.__eq__(outra)

# pessoa1 = Pessoa("Alice", 30)
# pessoa2 = Pessoa("Bob", 25)

# print(pessoa1 != pessoa2)  # Saída: True

# class ListaPersonalizada:
#     def __init__(self, itens):
#         self.itens = itens
    
#     def __len__(self):
#         return len(self.itens)

# minha_lista = ListaPersonalizada([1, 2, 3, 4, 5])
# tamanho = len(minha_lista)
# print(tamanho)  # Saída: 5



print("Fim!")
