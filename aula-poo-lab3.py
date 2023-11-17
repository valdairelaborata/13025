class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

    def alterarTitular(self, novoTitular):
        self.titular = novoTitular

    def consultarSaldo(self):
        print(self.saldo)


minha_conta = ContaBancaria("João", 1000)
minha_conta.consultarSaldo()
minha_conta.saldo = 50000
minha_conta.titular = "Valdair"
minha_conta.depositar(500)
minha_conta.consultarSaldo()
minha_conta.alterarTitular("Maria")
minha_conta.sacar(100)
minha_conta.consultarSaldo()

minha_conta.sacar(200)

