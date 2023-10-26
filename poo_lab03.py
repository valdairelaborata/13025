class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

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