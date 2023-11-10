import unittest

class ContaBancaria:

    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor


    def sacar(self, valor):
        self.__saldo -= valor


    def obter_saldo(self):
        return self.__saldo



class TesteContaBancaria(unittest.TestCase):

    def teste_deposito(self):
        conta = ContaBancaria(50)
        conta.depositar(50)
        self.assertEqual(conta.saldo, 100)

    def teste_sacar(self):
        conta = ContaBancaria(200)
        conta.sacar(50)
        self.assertEqual(conta.saldo, 150)
        
    def teste_consulta_saldo(self):
        conta = ContaBancaria(500)
        self.assertEqual(conta.obter_saldo(), 500)


unittest.main()

