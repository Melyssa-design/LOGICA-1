import os
os. system ("clear")
from dataclasses import dataclass

@dataclass
class funcionario:
    nome: str
    data_de_nascimento: str
    rg: str
    cpf: str

    def exibrir_dados(self):
        print(f"\nNome: {self.nome}, \nData de nascimento:{self.data_de_nascimento}, \nRG: {self.rg}, \nCPF: {self.cpf}")

lista_de_funcionarios = []
QUANTIDADE_DE_FUNCIONARIOS = 2

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    Funcionario = funcionario(
        nome = input("Digite seu nome: "),
        data_de_nascimento = input("Digite sua data de nascimento: "),
        rg = input("Digite seu RG: "),
        cpf = input("Digite seu CPF: ")
    )
    lista_de_funcionarios.append(Funcionario)
    os.system("clear")

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo_funcionario:
    for Funcionario in lista_de_funcionarios:
        arquivo_funcionario.write(f"\n{Funcionario.nome}\n{Funcionario.data_de_nascimento}\n{Funcionario.rg}\n{Funcionario.cpf}\n")
print("\nDados dos funcionarios salvos com sucesso")


try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado.")