#limpar terminal
import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário um valor e escrever a mensagem: É MAIOR QUE 10! 
# Se o valor lido for maior que 10, caso contrário escrever: NÃO É MAIOR QUE 10!

#solicitando dados
valor = int(input ("Digite um valor: "))

if valor > 10:
    print("É MAIOR QUE 10!")
else:
    print("NÃO É MAIOR QUE 10!")

print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")