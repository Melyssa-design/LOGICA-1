import os
from dataclasses import dataclass
os.system("cls || clear")

#Definindo classe.
@dataclass
class Pessoa():
    nome: str
    idade: int
    peso: float
    altura: float

pessoal = Pessoa ("Marta", 33, 55.333, 1.69)

print("Exibindo dados: ")
print (f"Nome: {pessoal.nome}, idade: {pessoal.idade}, peso: {pessoal.peso}, altura: {pessoal.altura}")