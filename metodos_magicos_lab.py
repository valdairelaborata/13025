class ContaBancaria:

    def __init__(self, numero, titular, saldo) :
        self.numero = numero
        self.titular = titular 
        self.saldo = saldo

    def __str__(self):
        return f'Conta de:{self.titular}: {self.saldo}'
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor



conta = ContaBancaria("12345", "João", 1000.0)
print(conta)    

conta.depositar(500.0)
print(conta)    

conta.sacar(200.0)
print(conta)  