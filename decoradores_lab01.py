
def autenticar(funcao):
    def wrapper():
        usuario_valido = True
        print('Verificar se usuário é válido')
        if usuario_valido:
            funcao()
        else:
            print('Usuário não autenticado!')
    return wrapper


@autenticar
def obter_cliente():
    print(f'Obtendo os dados do cliente')
    
@autenticar
def gerar_relatorio():
    print(f'Obtendo relatório do cliente')
    




obter_cliente()

gerar_relatorio()