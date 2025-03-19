import os
import time
os.system("cls | clear")

#Escrever um algoritmo que solicite ao usuário um
#número e faça a contagem regressiva a partir do
#número informado até o número 1, aguardando um
#segundo para exibir cada número.


numero = int(input("digite um numero: ")) 

for i in range(numero,0,-1):
    print(f"valor da variavel: {i}")
    time.sleep(1)