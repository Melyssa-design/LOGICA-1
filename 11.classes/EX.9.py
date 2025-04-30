import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_de_nascimento: str
    rg: str
    cpf: str

    def exibir_dados(self):
        print(f"\nNome: {self.nome}, \nData de nascimento:{self.data_de_nascimento}, \nRG: {self.rg}, \nCPF: {self.cpf}")

lista_de_funcionarios = []
QUANTIDADE_DE_FUNCIONARIOS = 2

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    funcionario = Funcionario(
            nome = input("Digite seu nome: "),
            data_de_nascimento = input("Digite sua data de nascimento: "),
            rg = input("Digite seu RG: "),
            cpf = input("Digite seu CPF: ")
        )
    lista_de_funcionarios.append(funcionario)
    os.system("clear") 

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo_funcionario:
    for funcionario in lista_de_funcionarios:
        arquivo_funcionario.write(f"\n{funcionario.nome}\n{funcionario.data_de_nascimento}\n{funcionario.rg}\n{funcionario.cpf}\n")

print("\nDados dos funcionarios salvos com sucesso")

print("\nExibindo os dados dos funcionarios")
for funcionario in lista_de_funcionarios:
    funcionario.exibir_dados()