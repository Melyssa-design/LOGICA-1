import os
import time
os.system ("clear")
from dataclasses import dataclass

@dataclass
class dados:
    nome: str
    cpf: str
    cargo: str
    salario: str

lista_funcionarios = []

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
    
funcionario = []

def exibir_menu():
    """
    Exibe o menu interativo para o usuário.
    """
    print("\n╔═══════════════════════════════════╗")
    print("║   Sistema de Cadastro DENDÊ TECH  ║")
    print("╠═══════════════════════════════════╣")
    print("║ 1. Cadastrar Funcionário          ║")
    print("║ 2. Listar Todos os Funcionários   ║")
    print("║ 3. Buscar Funcionário Específico  ║")
    print("║ 4. Atualizar Funcionário          ║")
    print("║ 5. Excluir Funcionário            ║")
    print("║ 6. Salvar Dados em CSV            ║")
    print("║ 7. Carregar Dados de CSV          ║")
    print("║ 8. Sair                           ║")
    print("╚═══════════════════════════════════╝")

    # --- Função Principal (main) ---
def main():
    """
    Função principal que executa o sistema.
    """
    print("Bem-vindo ao Sistema de Cadastro de Funcionários DENDÊ TECH!")
    carregar_dados_csv() # Carrega dados ao iniciar

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-8): ").strip()

        if escolha == '1':
            cadastrar_funcionario()
        elif escolha == '2':
            listar_funcionarios()
        elif escolha == '3':
            buscar_funcionario_especifico_interativo()
        elif escolha == '4':
            atualizar_funcionario()
        elif escolha == '5':
            excluir_funcionario()
        elif escolha == '6':
            salvar_dados_csv()
        elif escolha == '7':
    # Nome do arquivo CSV 


nome_do_arquivo = "funcionarios.csv"
with open(nome_do_arquivo, "a") as arquivos_funcionario:
    for funcionario in lista_funcionarios:
        arquivos_funcionario.write(f"\nNome: {funcionario.nome} \nCPF: {funcionario.cpf} \nCargo: {funcionario.cargo} \nSalario {funcionario.salario}")
    print(f"\nDados salvos no arquivo {nome_do_arquivo} com sucesso.")