from service.livro_service import LivroService

class LivroController:
    def __init__(self):
        self.service = LivroService()

    def listar_livros(self):
        return self.service.listar_livros()

    def comprar_livro(self, id):
        return self.service.comprar_livro(id)