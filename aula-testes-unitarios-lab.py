import unittest

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor

    def verificar_saldo(self):
        return self.saldo


class TesteContaBancaria(unittest.TestCase):

    def test_saldo_inicial(self):
        conta = ContaBancaria(200)
        self.assertTrue(conta.saldo == 200)

    def test_depositar(self):
        conta = ContaBancaria()
        conta.depositar(100)
        self.assertEqual(conta.verificar_saldo(), 100)

    def test_sacar_valido(self):
        conta = ContaBancaria(200)
        conta.sacar(50)
        self.assertEqual(conta.verificar_saldo(), 150)

    def test_saque_saldo_insuficiente(self):
        conta = ContaBancaria(100)
        with self.assertRaises(ValueError):
            conta.sacar(150)

if __name__ == '__main__':
    unittest.main()


