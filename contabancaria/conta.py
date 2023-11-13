class Conta:
    def __init__(self, numero, saldo) :
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        self.saldo -= valor

    def __str__(self):
        return f'Conta Nr: {self.numero} e tem {self.saldo} de saldo!'