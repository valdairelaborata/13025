class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def sacar(self, valor):
        self.__saldo -= valor

    def zerarSaldo(self):
         self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor


    def exibirSaldo(self):
        return f"Saldo atual {self.saldo}"



class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if self.saldo >= valor:
             super().sacar(valor)
        else:
            if self.saldo > 0:               
               self.__limite -= valor - self.saldo
               super().zerarSaldo()
            else:
                if self.__limite < valor:
                    print("Limite insuficiente!")
                else:
                    self.__limite -= valor 

        self.exibirSaldo()   

    def exibirSaldo(self):
        print(f"{super().exibirSaldo()} e vc tem um limite de {self.limite}")


contaCorrente = ContaCorrente("Valdair", 0, 200)

contaCorrente.depositar(100)

contaCorrente.sacar(260)
contaCorrente.sacar(40)
contaCorrente.sacar(10)

print("Fim!")