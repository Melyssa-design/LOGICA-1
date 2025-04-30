import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Paciente:
    #ATRIBUTOS: são variaveis que pertence a classe.
    nome: str
    idade: int
    #METODO: é uma função que pertence a classe.
    #ESTE METODO É PARA EXIBIR OS DADOS DO PACIENTE
    def exibir_dados(self):
        print(f"Nome: {self.nome}, \nIdade: {self.idade}\n\n")
#CRIANDO LISTA DE PACIENTES
lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

#ATRIBUINDO DADES AO PACIENTE.
for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
                    nome = input("Digite sue nome: "),
                    idade = int(input("Digite sua idade: "))
                )
    lista_de_pacientes.append(paciente)
#SALVANDO EM UM ARQUIVO COM .TXT
nome_arquivo = "Dados_do_paciente.txt"
#letra w para apagar a cada salvamento)
with open(nome_arquivo, "w") as arquivo_paciente:
    for paciente in lista_de_pacientes:
        arquivo_paciente.write(f"{paciente.nome}, {paciente.idade}\n")

print(f"Dados salvos com sucesso.")       


#EXIBINDO DADOS DO PACIENTE.
print("\nExibindo dados do paciente.")
for paciente in lista_de_pacientes:
    paciente.exibir_dados() 