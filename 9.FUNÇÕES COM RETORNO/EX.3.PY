import os
os.system ("cls | clear")
from datetime import date

#ESCREVA UM PROGRAMA QUE SOLICITE AO USUÁRIO O ANO DE NASCIMENTO E, ULTILIZANDO UMA FUNÇÃO. RETORNE COM A IDADE DO USÁRIO.

#def calcular_idade(ano_de_nascimento):
#    idade = 2025 - ano_de_nascimento
#    return idade              

#ano_de_nascimento = int(input("Digite o ano de seu nascimento: "))
#idade = calcular_idade(ano_de_nascimento)

def calcular_idade(ano_de_nascimento):
    idade = date.today().year - ano_de_nascimento
    return idade              

ano_de_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = calcular_idade(ano_de_nascimento)


print(f"Idade: {idade}")

#