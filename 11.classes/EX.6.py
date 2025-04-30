import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class paciente:
    #ATRIBUTOS: são variaveis que pertence a classe.
    nome: str
    idade: int
    #METODO: é uma função que pertence a classe.
    #ESTE METODO É PARA EXIBIR OS DADOS DO PACIENTE
    def exibir_dados(self):
        print(f"Nome: {self.nome}, \nIdade: {self.idade}\n\n")

#ATRIBUINDO DADES AO PACIENTE.
paciente1 = paciente(nome="Maria" , idade=30)

#EXIBINDO DADOS DO PACIENTE.
paciente1.exibir_dados()