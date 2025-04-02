import os

# FUNÇÃO SEM RETORNO
def logo_senai():
    os.system ("cls | clear")
    print("==SENAI==")

logo_senai() # CHAMANDO A FUNÇÃO
nome = (f" Digite seu nome: ")

logo_senai() #CHAMANDO A FUNÇÃO
idade = (f" Digite sua idade: ")

logo_senai() # CHAMANDO A FUNÇÃO
print (f"Nome:{nome}")
print(f"Idade: {idade}")
