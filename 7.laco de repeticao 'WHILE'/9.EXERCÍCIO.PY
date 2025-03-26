import os
os.system("clear")

#Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, 
#inseridos pelo usuário. 
#O final da leitura acontecerá quando for lido um valor negativo.
#Mostre a média aritmética dos números informados pelo usuário.

soma = 0
contador = 0

while True:
        nota = int(input("Digite sua nota: "))
        if nota < 0:
                break
        contador += 1
        soma += nota
  
if contador == 0:
        soma = nota
        contador = 1   

media = soma/contador




print(f"Media: {media}.")

#segunda forma
#while true:
#nota = int(input(f"Digite o {contador + 1}º numero:"))
