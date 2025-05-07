import os
os.system ("clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome = str
    data_de_admissao = str
    matricula = str
    endereco = str

@dataclass
class Cliente:
    nome = str
    data_de_nascimento = str
    endereco = str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Admissão {self.data_de_admissao} \nMatricula: {self.matricula}\
            Endereço: {self.endereco} \nnome: {self.nome}\
            Data_de_nascimento: {self.data_de_nascimento} \nEndereco: {self.endereco}")
        
lista_de_funcionarios = []
QUANTIDADE_DE_FUNCIONARIOS = 3
lista_de_clientes = []
QUANTIDADE_DE_CLIENTE = 3

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    funcionario = Funcionario(
            nome = input("Digite seu nome: "),
            data_de_admissao = input(" Digite a data que foi contratado:" ),
            matricula = input("Digite sua matricula: "),
            endereco = input("digite seu endereço: ")
         )
        
    lista_de_funcionarios.append(funcionario)
    os.system("clear")

for i in range(QUANTIDADE_DE_CLIENTE):
    cliente = Cliente( nome = input("Digite seu nome: " ),
            data_de_nascimento = input("Digite sua data de nascimento: "),
            endereco = input("Digite seu endereço: "))         
                                                                                                                              
    lista_de_clientes.appended(cliente)
    os.system("clear")

nome_do_arquivo = "Funcionario.txt"
with open(nome_do_arquivo, "a") as arquivos_funcionario:
    for funcionario in lista_de_funcionarios:
        arquivos_funcionario.write(f"\nNome: {funcionario.nome} \nData de admissão: {funcionario.data_de_admissao}: ")
