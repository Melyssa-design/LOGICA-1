import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    idade: int
    peso: float
    altura: float                                                                               
    
    def exibir_dados(self):
        print(f"Nome:\n{self.nome}, \nIdade: {self.idade}, \nPeso: {self.peso}, \nAltura: {self.altura}\n")

lista_de_usuarios = []
QUANTIDADE_DE_USUARIOS = 4

for i in range(QUANTIDADE_DE_USUARIOS):
    usuario = Usuario(
            nome = input("\nDigite seu nome: "),
            idade = int(input("Digite sua idade: " )),
            peso = float(input("Digite sue peso: " )),
            altura = float(input("Digite sua altura: ")) 
            )    
    lista_de_usuarios.append(usuario)
    os.system("clear")

print("\nExibindo dados do usuário.")
for usuario in lista_de_usuarios:
    usuario.exibir_dados()

