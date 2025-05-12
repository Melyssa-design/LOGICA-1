import os
os.system("clear")
from dataclasses import dataclass


@dataclass
class funcionario:
    nome: str
    data_de_nascimento: str
    cpf: str
    funcao: str

    
def exibir_dados(self):
        print(f"Nome: {self.nome}, Data de Nascimento: {self.data_de_nascimento}, CPF: {self.cpf}, Função: {self.funcao}")
    
lista_funcionarios = []
    
for i in range():
        Funcionario = funcionario
        
        def verificar_lista_vazia(lista_funcionarios):
            if not lista_funcionarios:
                 print("\nA lista está vazia.")
                 return True
            return False
        
    
        def adicionar_funcionario(lista_funcionario):
            nome = input("Digite o nome do funcionário: ")
            data_de_nascimento = input("Digite a data de nascimento do funcionário: ")
            cpf = input("Digite o CPF do funcionário: ")
            funcao = input("Digite a função do funcionário: ")
            lista_funcionario.append(nome, data_de_nascimento, cpf, funcao)
            print(f"\Cadastro do funcionário {nome} realizado com sucesso.")

        def mostrar_funcioinarios(lista_funcionarios):
             if funcionario.verificar_lista_vazia(lista_funcionarios):
                return
        ("\n - lista de funcionários" )


        print("\n - Lista de funcionários")
        for funcionario in lista_funcionarios:
            print(f" - Nome: ^{funcionario.nome}, Data de Nascimento: {funcionario.data_de_nascimento}, CPF: {funcionario.cpf}, Função: {funcionario.funcao}")

        def mostrar_funcionarios(lista_funcionarios):
            nome_antigo = input("Digite o nome di funcionario que deseja atualizar: ")
            if nome_antigo in lista_funcionarios:
                novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
                indice = lista_funcionarios.index(nome_antigo)
                lista_funcionarios[indice] = novo_nome
                print(f"{nome_antigo} foi atualizado para {novo_nome}.")
            else:
                print(f"\nO nome {nome_antigo} não foi encontrado.")
                return
    
        def atualizar_nome_do_funcionario(lista_funcionarios):
             if funcionario.verificar_lista_vazia(lista_funcionarios):
              return
        
        mostrar_funcionarios(lista_funcionarios)
        nome_antigo = input("Digite o nome do funcionario que deseja atualizar: ")
        if nome_antigo in lista_funcionarios:
            novo_nome = input(f"Digite o novo nome para {nome_antigo}")
            indice = lista_funcionarios.index(nome_antigo)
            lista_funcionarios[indice] = novo_nome
            print(f"{nome_antigo} foi atualizado para {novo_nome}.")
        else:
            print(f"\nO nome {nome_antigo} não foi encontrado.")
            
    
        def excluir_funcionario(lista_funcionarios):
            if funcionario.verificar_lista_vazia(lista_funcionarios):
                return
        
            mostrar_funcionarios(lista_funcionarios)

            nome_remover = input("Digite o nome do funcionario que deseja remover: ")
            if nome_remover in lista_funcionarios:
                lista_funcionarios.remove(nome_remover)
                print(f"O nome {nome_remover} foi removido com sucesso.")
            else:
              print(f"O nome {nome_remover} não foi encontrado.")
       
nomes = []

while True:
        print("""_DADOS DO FUNCIONÁRIO_
              1 - Adicionar
              2 - Listar funcionarios
              3 - Atualizar
              4 - Excluir
              5 - Sair
              """)
        opcao = input("Escolha uma opçao: ")
    
        match opcao:
            case 1:
                adicionar_funcionario(nomes)
            case 2: 
                mostrar_funcionarios(nomes)
            case 3:
                atualizar_nome_do_funcionario(nomes)
            case 4:
                excluir_funcioinario(nomes)
            case 5:
                print("\nSaindo do programa.")
                break
            case _:
                print("\nOpção inválida.\nTente novamente.")