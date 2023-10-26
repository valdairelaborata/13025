class ContaBancaria:

    def __init__(self, nome, valor):
        self.titular = nome
        self.saldo = valor

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor


contaA = ContaBancaria("João", 0)
contaA.depositar(10)
print(contaA.saldo)

contaA.sacar(20)
print(contaA.saldo)