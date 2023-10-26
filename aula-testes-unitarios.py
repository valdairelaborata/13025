import unittest

def soma(a, b):
    return a + b 

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
       raise ZeroDivisionError("Não é possível dividir por zero")
    return a / b



class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        resultado = soma(5, 3)
        self.assertEqual(resultado, 8)

    def test_subtracao(self):
        resultado = subtracao(5, 3)
        self.assertEqual(resultado, 2)

    def test_multiplicacao(self):
        resultado = multiplicacao(5, 3)
        self.assertEqual(resultado, 15)

    def test_divisao(self):
        resultado = divisao(6, 2)
        self.assertEqual(resultado, 3)

        with self.assertRaises(ZeroDivisionError):
            divisao(5, 0)

if __name__ == '__main__':
    unittest.main()
