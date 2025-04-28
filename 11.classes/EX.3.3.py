import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Pessoa():
    nome: str
    email: str
    telefone: float
    endereco: float
    
    def exibindo_dados(self):
        print(f"\nExibindo dados:")
        print(f"nome: {self.nome}, email: {self.email}, telefone: {self.telefone} endereço: {self.endereco}")


nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

pessoa1 = Pessoa(nome, email, telefone, endereco)
pessoa1.exibindo_dados()