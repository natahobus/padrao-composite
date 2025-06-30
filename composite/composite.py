from abc import ABC, abstractmethod

class ItemSistema(ABC):
    @abstractmethod
    def exibir(self, nivel=0):
        pass

class Arquivo(ItemSistema):
    def __init__(self, nome):
        self.nome = nome

    def exibir(self, nivel=0):
        print("  " * nivel + f"Arquivo: {self.nome}")

class Pasta(ItemSistema):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item: ItemSistema):
        self.itens.append(item)

    def exibir(self, nivel=0):
        print("  " * nivel + f"Pasta: {self.nome}")
        for item in self.itens:
            item.exibir(nivel + 1)

# Teste
if __name__ == "__main__":
    arq1 = Arquivo("relatorio.pdf")
    arq2 = Arquivo("imagem.png")

    pasta1 = Pasta("Documentos")
    pasta1.adicionar(arq1)
    pasta1.adicionar(arq2)

    pasta2 = Pasta("Projetos")
    pasta2.adicionar(pasta1)
    pasta2.adicionar(Arquivo("projeto.docx"))

    pasta2.exibir()
