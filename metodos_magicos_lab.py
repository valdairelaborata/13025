class ContaBancaria:

    def __init__(self, numero, titular, saldo) :
        self.__numero = numero
        self.__titular = titular 
        self.__saldo = saldo

    def __str__(self):
       return f'Conta Nr:{self.__numero} do titular:{self.__titular}: com: {self.__saldo} de saldo'
    
    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

    def __eq__(self, conta):
        return self.__numero == conta.__numero 

    def  __ne__(self, conta):
        return not self.__eq__(conta)


conta1 = ContaBancaria("12345", "João", 1000.0)
conta2 = ContaBancaria("12346", "João", 1000.0)

print(conta1 == conta2)

print(conta1.saldo)    

conta1.depositar(500.0)
print(conta1)    

conta1.sacar(200.0)
print(conta1)  