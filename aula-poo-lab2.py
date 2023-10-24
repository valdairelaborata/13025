class Calculadora:
    def __init__(self) -> None:
        pass

    def adicionar(self, a, b):
        self.a = a
        return f"O resultado da soma é: {a + b}"
        #return f"O resultado da soma é: {self.a + self.b}"
    
    def subtrair(self, a, b):
        return f"O resultado da subtração é: {a - b}"
    
    def multiplicar(self, a, b):
        return f"O resultado da multiplicação é: {a * b}"
    

minha_calculadora = Calculadora()
print(minha_calculadora.adicionar(10, 5))
print(minha_calculadora.subtrair(10, 5))
print(minha_calculadora.multiplicar(10, 5))
