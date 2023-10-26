class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__outraInformacao = "teste"

    def depositar(self, valor):
        self.__saldo += valor
      

    def consultarOutraInformacao(self):
        print(self.__outraInformacao)

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor

    def alterarTitular(self, novoTitular):
        self.__titular = novoTitular

    def consultarSaldo(self):
        print(self.__saldo)

    def consultarTitular(self):
        print(self.__titular)


minha_conta = ContaBancaria("João", 1000)
minha_conta.consultarSaldo()
minha_conta.consultarOutraInformacao()

minha_conta.depositar(500)


minha_conta.consultarSaldo()
minha_conta.alterarTitular("Maria")
minha_conta.consultarTitular()
minha_conta.sacar(100)
minha_conta.consultarSaldo()

print("Fim!")

