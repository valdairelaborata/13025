
class Pessoa(object):

    def __init__(self, nome):
        self.__nome = nome


    def __del__(self):
        print(f'Objeto {self.__nome} está sendo excluído')


    def __str__(self):
        return f'Olá, eu sou {self.__nome}'
        

pessoa1 = Pessoa("João")

# del pessoa1

print(pessoa1)




print('Fim')