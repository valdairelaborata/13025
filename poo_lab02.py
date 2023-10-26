class Calculadora:

    def __init__(self, resultado = 0.0):
        self.resultado = resultado

    def adicao(self, valor1, valor2):
        self.resultado = valor1 + valor2

    def subtracao(self, valor1, valor2):    
        self.resultado = valor1 - valor2

    def multiplicacao(self, valor1, valor2):    
        self.resultado = valor1 * valor2
        
    def  divisao(self, valor1, valor2):    
        self.resultado = valor1 / valor2


minhaCalculadora = Calculadora()
minhaCalculadora.adicao(10, 15)
print(minhaCalculadora.resultado)

minhaCalculadora.subtracao(10, 15)
print(minhaCalculadora.resultado)

minhaCalculadora.multiplicacao(10, 15)
print(minhaCalculadora.resultado)

minhaCalculadora.divisao(10, 15)
print(minhaCalculadora.resultado)