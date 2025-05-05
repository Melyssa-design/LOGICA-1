import os
os.system ("clear")
from dataclasses import dataclass

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_dados(self):
        print("Nome: {self.nome} Biografia: {self.biografia} Titulo: {self.titulo} Ano: {self.ano}")

lista_de_livros = []
QUANTIDADE_DE_LIVROS = 1

for i in range(QUANTIDADE_DE_LIVROS):   
    livro = Livro(
        titulo = input("Digite o titulo do livro: "), 
        ano = int(input("Digite o ano de lançamento do livro: ")),
        autor = Autor
        (nome = input("Digite o nome do autor: ")),
        biografia = input("Digite a biografia do autor: "))

    
    lista_de_livros.append(livro)


print("Salvando dados")

nome_arquivo = "literatura.txt"
with open(nome_arquivo, "a") as arquivo_livro:
    for livro in lista_de_livros:
        arquivo_livro.write(f"{livro.nome}, {livro.titulo}, {livro.ano},{livro.autor.nome}")

print("\nDados dos livros salvos com sucesso")