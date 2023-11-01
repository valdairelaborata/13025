class ListaPersonalizada:

    def __init__(self, itens):
        self.itens = itens

    def __len__(self):
        return len(self.itens)

    def __str__(self):
        return f'Olá, eu sou a lista personalizada e tenho {len(self)} itens.'


minha_lista = ListaPersonalizada([1, 2, 3, 4, 5, 6])
print(minha_lista)

print('Fim')
