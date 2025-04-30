import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Autor: {self.autor}, Categoria: {self.categoria}, Preço: {self.preco}")
lista_de_livros = []
QUANTIDADE_DE_LIVROS = 1
for i in range(QUANTIDADE_DE_LIVROS):
    livro = Livro(
            nome = input("Digite o nome do livro: "),
            autor = input("Digite o nome do autor: "),
            categoria = input("Digite qual categoria pertence o livro: "),
            preco = float(input("Digite o valor do livro:"))
        )
    lista_de_livros.append(livro)
    os.system("clear")

#SALVANDO EM UM ARQUIVO .TXT
nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as arquivo_livro:
    for livro in lista_de_livros:
        arquivo_livro.write(f"\n{livro.nome}, \n{livro.autor}, \n{livro.categoria}, \n{livro.preco}\n")

print("\nDados dos livros salvos com sucesso")
          
print("\nExibindo os dados dos livros")
for livro in lista_de_livros:
    livro.exibir_dados()