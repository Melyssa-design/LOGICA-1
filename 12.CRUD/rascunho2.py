import os
import time
import csv

os.system ("clear")
from dataclasses import dataclass

@dataclass
class dados:
    nome: str
    cpf: str
    cargo: str
    salario: str

lista_funcionarios = []


# Função para salvar os dados em um arquivo CSV.
def salvar_funcionarios(arquivo='funcionarios.csv'):
    with open(arquivo, "a") as arquivo_funcionario:
        writer = csv.writer(arquivo_funcionario)
        for funcionario in lista_funcionarios:
            arquivo_funcionario.write([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario])
        print("\nDados salvos com sucesso.")

    
    # Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios: 
        print("\nA lista está vazia.")
        return True
    return False 

def listar_funcionario():
    if verificar_lista_vazia(lista_funcionarios):
        return
    print("\n - Lista de funcionários - ")
    for funcionario in lista_funcionarios:
        print(f"- Nome: {funcionario.nome}, \nCPF: {funcionario.cpf}, \nCargo: {funcionario.cargo}, \nSalário: {funcionario.salario}")

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = input ("Digite o salario do funcionáorio: ")
    lista_funcionarios.append(dados(nome, cpf, cargo, salario))
    print(f"\nFuncionário {nome} cadastrado com sucesso.")
    
  
def listar_funcionario():
    if verificar_lista_vazia(lista_funcionarios):
        return
    print("\n _Lista de funionarios_")
    for funcionario in lista_funcionarios:
        print(f"- \nNome: {funcionario.nome} \nCPF: {funcionario.cpf} \nCargo: {funcionario.cargo} \nSalário: {funcionario.salario}")
    
def atualizar_funcionario():
    if verificar_lista_vazia(lista_funcionarios):
        return
    listar_funcionario()
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_funcionarios: # Verificar se o nome existe na lista.
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
        novo_cpf = input(f"Digite o novo CPF para {nome_antigo}: ")
        novo_cargo = input(f"Digite o novo cargo para {nome_antigo}: ")
        novo_salario = input(f"Digite o novo salário para {nome_antigo}: ")
        indice = lista_funcionarios.index(nome_antigo)
        lista_funcionarios[indice] = dados(novo_nome, novo_cpf, novo_cargo, novo_salario) # Atualiza os dados do funcionário.
        print(f"{nome_antigo} foi atualizado para {novo_nome}.")

def excluir_funcionario():
    if verificar_lista_vazia(lista_funcionarios):
        return
    listar_funcionario()
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_funcionarios: # Verifica se o nome existe na lista.
        lista_funcionarios.remove(nome_remover) # Remove o funcionário da lista.
        print(f"{nome_remover} foi removido com sucesso.")
    else:
        print(f"O nome {nome_remover} não foi encontrado.")

funcionario = []

while True:
    print("""
    - Gerenciador de nomes -
    1 - Cadastrar
    2 - Listar nomes
    3 - Atualizar 
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            cadastrar_funcionario()
        case 2:
            listar_funcionario()
        case 3:
            atualizar_funcionario()
        case 4:
            ...
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
            time.sleep(5)


   