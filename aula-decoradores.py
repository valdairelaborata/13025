# def aplicar_operacao(operacao, numeros):
#     return [operacao(numero) for numero in numeros]

# def dobrar(x):      
#     return x * 2

# def triplicar(x):
#     return x * 3

# numeros = [1, 2, 3, 4, 5]

# numeros_dobrados = aplicar_operacao(dobrar, numeros)

# numeros_triplicados = aplicar_operacao(triplicar, numeros)

# print("Números dobrados:", numeros_dobrados)
# print("Números triplicados:", numeros_triplicados)


# def meu_decorator(funcao):
#     def wrapper(*args, **kwargs):
#         print("Antes da chamada da função")
#         resultado = funcao(*args, **kwargs)
#         print("Depois da chamada da função")
#         return resultado
#     return wrapper
# @meu_decorator
# def minha_funcao():
#     print("Executando minha função")

# minha_funcao()


# def verificarEstoque(fazerVenda):
#     def verificar(*args, **kwargs):
#         print("Consultar estoque.")
#         resultado = fazerVenda(*args, **kwargs)
#         return resultado
#     return verificar

# @verificarEstoque
# def fazerVenda():
#     print("Fazer a venda....")


# fazerVenda()






def meu_decorator(funcao):
    def wrapper(*args, **kwargs):
        print("Antes da chamada da função")
        resultado = funcao(*args, **kwargs)
        print("Depois da chamada da função")
        return resultado
    return wrapper

# @meu_decorator
# def minha_funcao():
#     print("Executando minha função")


@meu_decorator
def minha_outra_operacao():
    print("Minha outra operação")

minha_outra_operacao()




