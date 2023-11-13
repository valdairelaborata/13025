
from datetime import datetime

import math
from Recursos_Humanos.Colaborador import Colaborador
from cadastro.Pessoa import Pessoa
from cadastro.Produto import Produto

from calculadora.calculo import somar, subtrair
from financeiro.contas_pagar import ContasPagar

pessoa = Pessoa("Maria")
print(pessoa)

produto = Produto("xpto 0100")
print(produto)


soma = somar(10, 5)
print(soma)

valor_sutraido = subtrair(20, 5)
print(valor_sutraido)



# Raiz quadrada
raiz_quadrada = math.sqrt(16)  # Retorna 4.0

# Potência
potencia = math.pow(2, 3)  # Retorna 8.0

# Valor absoluto
absoluto = math.fabs(-5)  # Retorna 5.0

# Arredondamento
arredondado = round(4.7)  # Retorna 5


agora = datetime.now()
print(agora)

contas_pagar = ContasPagar()

print(contas_pagar)

colaborador = Colaborador()
