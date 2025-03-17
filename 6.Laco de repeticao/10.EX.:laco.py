import os
os.system("cls | clear")

#Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.

soma = 0

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota 

media = soma /4

print(f"Media {media}")