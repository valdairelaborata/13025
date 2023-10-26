class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Conta de {self.titular}: {self.saldo}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
            

conta1 = ContaBancaria(12345, "João", 1000)
print(conta1)

conta1.depositar(500)
print(conta1)

conta1.sacar(300)
print(conta1)

conta1.sacar(1500)  # Tenta sacar um valor maior que o saldo
print(conta1)


