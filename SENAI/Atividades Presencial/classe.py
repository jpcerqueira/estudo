class Livros:
    def __init__(self, nome, autor, preco):
        self.nome = nome # parametro 'self.nome'
        self.autor = autor
        self.preco = preco

livros =[]
nome = input("Digite o nome")
autor = input("Digite o autor")
preco = input("Digite o preço")
livro1 = Livros(nome, autor, preco) # instancia 1
livro2 = Livros("Serpente do Mal", "Caio J.", 45.23)
livros = [livro1]

print(livro1.nome)

print(f"O livro {livro1.nome} do autor {livro1.autor} tem um valor de R$ {livro1.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
