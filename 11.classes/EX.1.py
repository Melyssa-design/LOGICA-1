import os
os.system ("clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int


@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

#Atribuindo valores.
pessoal = Pessoa ("Marta", 30)
pessoa2 = Pessoa("José", 40)
pet2 = Pet("Hulk", 6, "Pitbull")
pet1 = Pet("Toto", 4, "Pastor-alemão")

print("Dados da pessoas: ")
print (f"Nome: (pessoal.nome), idade: (pessoal. idade)")
print (f"Nome: (pessoa2.nome), idade: (pessoa2.idade)")
print("\nDados dos pets: ");
print (f"Nome: (petl.nome), idade: (petl.idade), raça: (petl.raca)")
print (f"Raça: (pet2.raca), nome: (pet2.nome), idade: (pet2.idade)")