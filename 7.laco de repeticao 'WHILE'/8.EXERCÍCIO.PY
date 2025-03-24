import os
os.system("clear")
#Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota, 
#se a resposta do usuário for “N”, 
#o programa fará a média aritmética das notas informadas 
#e mostrará a média aritmética para o usuário.
#Obs.: Use um contador dentro do laço de repetição para contar a
#quantidade de iterações (loops).

soma= 0
media = 0
contador = 0

while True:
        nota = float(input("Digite sua nota: "))
        continuar = input("Deseja inserir mais uma nota ?\n 'sim' ou 'não' : ")
        if continuar == "não":
                break
        contador += 1
        soma += nota

#evitar divisão por zero
if contador == 0:
        soma = nota
        contador = 1   

media = soma/contador

print(f"Media: {media}")

