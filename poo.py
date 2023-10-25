class Carro:

    def __init__(self, cor, placa, status, tipo):
        self.cor = cor
        self.placa = placa
        self.status = status
        self.tipo = tipo

    def ligar(self):
        self.status = "ligado"

    def desligar(self):
        self.status = "desligado"


celta = Carro("Preta", "AKS-3256", "desligado", "hatch")
camarroHatch = Carro("Azul", "AKS-3256", "desligado", "sedan")
civicao = Carro("Azul", "MDF-3296", "desligado", "sedan")

print(celta.ligar())
print(camarroHatch.ligar())
print(civicao.ligar())
