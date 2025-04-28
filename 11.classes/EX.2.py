import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade: int
    peso:float
    altura: float
    
nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
peso = float (input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

pessoa1 = Pessoa(nome,idade,peso,altura)
pessoa2 = Pessoa(idade=idade,nome=nome,peso=peso,altura=altura)

print(f"nome: {pessoa1.nome}, idade: {pessoa1.idade}, peso: {pessoa1.peso}, altura: {pessoa1.altura}")
print(f"nome: {pessoa2.nome}, idade: {pessoa2.idade}, peso: {pessoa2.peso}, altura: {pessoa2.altura}" )