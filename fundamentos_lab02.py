class ContaBancaria:

    def __init__(self, saldo, titular) :
        self.__saldo = saldo
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo


    def depositar(self, valor):
        self.__saldo += valor


    def sacar(self, valor):
        self.__saldo -= valor


    def trocarTitular(self, titular):
        self.__titular = titular

    
    def detalhes(self):
        return f'Conta do titular:{self.__titular}, com  saldo de:{self.__saldo}'


    def zerarSaldo(self):
        self.__saldo = 0


class ContaCorrente(ContaBancaria):

    def __init__(self, saldo, titular, limite):
        super().__init__(saldo, titular)
        self.__limite = limite


    def sacar(self, valor):
        if self.saldo >= valor:
            super().sacar(valor)
        else:
            if self.saldo > 0:
                self.__limite -= valor - self.saldo
                super().zerarSaldo()
            else:
                if self.__limite < valor:
                    print('Limite insuficiente!')
                else:    
                    self.__limite -= valor

    def detalhes(self):
        return super().detalhes() + f' e tem {self.__limite} de limite'
       



# cb = ContaBancaria(0, 'Valdair')
# cb.depositar(20)
# cb.sacar(15)
# print(cb.detalhes())


cc = ContaCorrente(0, 'João', 500)
cc.depositar(100)
cc.sacar(50)
cc.sacar(100)
cc.sacar(150)
print(cc.detalhes())












# conta01 = ContaBancaria(0, 'Valdair')
# print(conta01.detalhes())

# conta01.depositar(20)
# conta01.sacar(15)
# print(conta01.detalhes())

# conta01.trocarTitular('João')
# print(conta01.detalhes())

# conta01.depositar(200)
# conta01.sacar(150)
# print(conta01.detalhes())



