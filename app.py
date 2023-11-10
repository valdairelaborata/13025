import unittest

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

    def apresentacao(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos."
    
    def obter_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"



class TestePessoa(unittest.TestCase):

    def teste_apresentar(self):
        pessoa = Pessoa("João", "Silva", 25)
        apresentacao = pessoa.apresentacao()
        self.assertEqual(apresentacao, "Olá, eu sou João e tenho 25 anos.")

    def teste_obter_nome_completo(self):
        pessoa = Pessoa("João", "Silva", 25)
        nome_completo = pessoa.obter_nome_completo()
        self.assertEqual(nome_completo, "João Silva")


        



unittest.main()        