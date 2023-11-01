
class Numero:

    def  __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        novo_valor = self.valor + outro.valor
        return Numero(novo_valor)
    
    def __str__(self):
        return f'Olá, eu sou o número: {self.valor}'
      



numero1 = Numero(5)
numero2 = Numero(10)
resultado = numero1 + numero2

print(resultado)

print('Fim')