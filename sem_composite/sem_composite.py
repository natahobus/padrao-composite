class Arquivo:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self, nivel=0):
        print("  " * nivel + f"Arquivo: {self.nome}")


class Pasta:
    def __init__(self, nome):
        self.nome = nome
        self.arquivos = []

    def adicionar_arquivo(self, arquivo):
        self.arquivos.append(arquivo)

    def exibir(self, nivel=0):
        print("  " * nivel + f"Pasta: {self.nome}")
        for arquivo in self.arquivos:
            if isinstance(arquivo, Arquivo):
                arquivo.exibir(nivel + 1)
            else:
                print("  " * (nivel + 1) + "[ERRO]")


# Teste
arquivo1 = Arquivo("documento.txt")
arquivo2 = Arquivo("foto.jpg")

pasta_principal = Pasta("Meus Arquivos")
pasta_principal.adicionar_arquivo(arquivo1)
pasta_principal.adicionar_arquivo(arquivo2)

# Aqui começa a tentativa de hierarquia, que falha
pasta_interna = Pasta("Projetos")
pasta_interna.adicionar_arquivo(Arquivo("script.py"))

pasta_principal.adicionar_arquivo(pasta_interna)  # Isso gera erro na exibição

pasta_principal.exibir()
