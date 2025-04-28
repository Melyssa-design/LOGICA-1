import os
from dataclasses import dataclass
os.system( "clear")

@dataclass
class endereco:
    lagradouro: str
    numero: int

@dataclass
class pessoa:
    #Atributos da classe (variáveis que pertecem a uma classe)
    nome: str
    idade: int
    endereco: float

    #Metodos da classe (funções que pertecem a uma classe)
    def exibir_dados(self):
        print(f"nome: {self.nome}\
        idade: {self.idade}\
        lagradouro: {self.endereco.lagradouro}\
        numero: {self.endereco.numero}")

endereco1 = endereco("rua 1", "123")
pessoa1 = pessoa("Maria", 23, endereco1)

print("Exibindo dados:")
pessoa1.exibir_dados()