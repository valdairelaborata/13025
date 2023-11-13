

from contabancaria.conta import Conta


conta = Conta("321321", 0)
conta.deposito(50)
conta.saque(20)

print(conta)