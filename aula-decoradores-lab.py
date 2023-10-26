

def verificar_autenticacao(funcao):
    def wrapper(*args, **kwargs):
        usuario_autenticado = True  # Simule que o usuário está autenticado
        if usuario_autenticado:
            resultado = funcao(*args, **kwargs)
            return resultado
        else:
            print("Usuário não autenticado. Ação não permitida.")
    return wrapper


def validar_autenticacao(funcao):
    def verificarToken():
        usuario_autenticado = True  # Simule que o usuário está autenticado
        if usuario_autenticado:
            resultado = funcao()
            return resultado
        else:
            print("Usuário não autenticado. Ação não permitida.")
    return verificarToken



@validar_autenticacao
def buscar_pedido():    
    print("opa, agora vou buscar o pedido")
    #print(f"Buscar de pedido {valor1} {valor2}!!!")


buscar_pedido()


