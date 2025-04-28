import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereço: str

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereço = input("Digite seu endereço: ")

pessoa1 = Pessoa(nome,email,telefone,endereço)
print(f"nome: {pessoa1.nome}, email: {pessoa1.email}, telefone: {pessoa1.telefone}, endereço: {pessoa1.endereço}")