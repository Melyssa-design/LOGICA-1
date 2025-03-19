import os
os.system("cls | clear")

#Escrever um programa de computador que solicite do usuário 3 notas e, ao final,
#apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. 
#Considere que para aprovação, deve-se obter média maior ou igual a 7, 
#para ser reprovado, a média deve ser menor que 4.

soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota 

media = soma /3
if media >=7:
    print("Aprovado")
elif media < 4:
    print("reprovado")

print(f"Media {media}")