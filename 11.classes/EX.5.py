import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class endereco:
    lagradouro: str
    numero: str
    cidade: str

@dataclass
class pessoa:
    nome: str
    email: str
    endereco: endereco
    
    def exibir_dados(self):
        print(f"\tnome: {self.nome}\n"
              f"\temail: {self.email}\n"
              f"\tlagradourro: {self.endereco.lagradouro}" 
              f"\tnumero: {self.endereco.numero}"
              f"\tcidade: {self.endereco.cidade}")

nome = input ("Digite seu nome: ")
email = input ("Digite seu email: ")
lagradouro = input("Digite seu lgradouro: ")
numero = input("Digite o número da sua casa:")
cidade = input("Digite sua cidade:")

endereco1 = endereco(lagradouro, numero, cidade)
pessoa1 = pessoa( "nome" ,"email", endereco1)

print("exibir dados:")
pessoa1.exibir_dados()