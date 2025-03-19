import os
os.system("cls | clear")

#Escrever um programa de computador que solicite do usuário 5 números inteiros e,
#  ao final, apresente a soma de todos os números lidos.

soma = 0
for i in range(5):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    soma = soma + nota
    
print(f"Soma: {soma}")