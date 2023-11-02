
def meu_decorador(funcao):
    def wrapper():
        print('Antes da função')
        funcao()
        print('Depois da função')

    return wrapper


@meu_decorador
def minha_funcao():
    print('Minha função')


@meu_decorador
def minha_segunda_funcao():
    print('Segunda função')


minha_funcao()

minha_segunda_funcao()

