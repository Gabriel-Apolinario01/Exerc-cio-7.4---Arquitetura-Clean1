from model.livro import LivroModel

compras = []

class LivroService:
    def __init__(self):
        self.model = LivroModel()

    def listar_livros(self):
        return self.model.listar_livros()

    def comprar_livro(self, id):
        livro = self.model.listar_livros()[id]
        compras.append(livro)
        return livro

    def listar_compras(self):
        return compras