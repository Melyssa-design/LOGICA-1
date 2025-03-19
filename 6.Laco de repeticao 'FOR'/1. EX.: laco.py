import os
os.system("cls | clear")

#laço de repetição: for
numero = int(input("Digite um numero para tabuada:"))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

