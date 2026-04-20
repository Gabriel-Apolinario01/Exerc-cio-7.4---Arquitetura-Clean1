from flask import Flask, render_template
from controller.livro_controller import LivroController

app = Flask(__name__)
controller = LivroController()


@app.route("/")
def home():
    livros = controller.listar_livros()
    return render_template("index.html", livros=livros)


@app.route("/comprar/<int:id>")
def comprar(id):
    livro = controller.comprar_livro(id)
    return render_template("compra.html", livro=livro)


# HISTÓRICO
@app.route("/compras")
def compras():
    compras = controller.service.listar_compras()
    return render_template("compras.html", compras=compras)


if __name__ == "__main__":
    app.run(debug=True)