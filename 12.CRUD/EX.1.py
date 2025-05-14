import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

funcionarios = []

def menu():
    print("\n--- MENU ---")
    print("1. Adicionar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Remover Funcionário")
    print("5. Sair")

def adicionar_funcionario():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    funcao = input("Função: ")
    funcionario = Funcionario(nome, data_nascimento, cpf, funcao)
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso.")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for idx, func in enumerate(funcionarios):
            print(f"{idx + 1}. {func}")

def atualizar_funcionario():
    listar_funcionarios()
    try:
        idx = int(input("Informe o número do funcionário a ser atualizado: ")) - 1
        if 0 <= idx < len(funcionarios):
            func = funcionarios[idx]
            print("Deixe em branco para manter o valor atual.")
            nome = input(f"Novo nome ({func.nome}): ") or func.nome
            data_nascimento = input(f"Nova data de nascimento ({func.data_nascimento}): ") or func.data_nascimento
            cpf = input(f"Novo CPF ({func.cpf}): ") or func.cpf
            funcao = input(f"Nova função ({func.funcao}): ") or func.funcao
            funcionarios[idx] = Funcionario(nome, data_nascimento, cpf, funcao)
            print("Funcionário atualizado com sucesso.")
        else:
            print("Funcionário não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def remover_funcionario():
    listar_funcionarios()
    try:
        idx = int(input("Informe o número do funcionário a ser removido: ")) - 1
        if 0 <= idx < len(funcionarios):
            removido = funcionarios.pop(idx)
            print(f"Funcionário {removido.nome} removido com sucesso.")
        else:
            print("Funcionário não encontrado.")
    except ValueError:
        print("Entrada inválida.")


while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        adicionar_funcionario()
    elif opcao == '2':
        listar_funcionarios()
    elif opcao == '3':
        atualizar_funcionario()
    elif opcao == '4':
        remover_funcionario()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")