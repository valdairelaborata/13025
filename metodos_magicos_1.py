
class Pessoa(object):

    def __init__(self, nome):
        self.__nome = nome


    def __del__(self):
        print(f'Objeto {self.__nome} está sendo excluído')


    def __str__(self):
        return f'Olá, eu sou {self.__nome}'
    
    def __repr__(self):
        return f'Pessoa(nome:{self.__nome})'

    def __eq__(self, outro):
        return self.__nome == outro.__nome 
    
    def  __ne__(self, outro):
        return not self.__eq__(outro)
       

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

print(pessoa1 == pessoa2)

print(pessoa1 != pessoa2)


# del pessoa1

# print(pessoa1)
# print(repr(pessoa1))



print('Fim')