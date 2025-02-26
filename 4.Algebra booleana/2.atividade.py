import os

from numpy import rint
os.system("clear")

#Elabore um algoritmo usando operações lógicas para informar se uma pessoa é obrigada a votar.
#Considere que a regra é que menores de 18 e maiores que 65 não são obrigados a votar.

idade = int(input("Digite sua idade: "))
    
 # OPÇÃO 1
if idade < 18 or idade > 65:
        print("Não é obrigatório votar")
else:
        print("É obrigatório votar!")

print(f"Idade:{idade}")

# OPÇÃO 2
# if idade >= 18 and idade <= 65:
#    resultado = "É obrigatorio votar."
# else:
#    resultado = "Não é obrigatorio votar"
print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")