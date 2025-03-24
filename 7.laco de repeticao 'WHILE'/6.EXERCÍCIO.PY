import os
os.system("cls | clear")
#Escreva um algoritmo que leia três notas de um aluno.
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, 
# recuperação ou reprovado considerando os seguintes critérios: 
#Se a média for a partir de 7, aprovado; 
#Se a média for entre 5 e 6,9, o aluno está em recuperação; 
#Caso seja menor que 5, o aluno está reprovado.

QUANTIDADE_DE_NOTAS = 3
soma= 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input("Digite sua nota: "))
        
        if nota < 0 or nota > 10:
            print("Nota invalida. \nTente novamente")
        else:
            soma += nota
            break
media = soma / QUANTIDADE_DE_NOTAS

if media >= 7:
    resultado = "Aprovado" 
elif media >= 5:
    resultado= "Recuperação"
else:
    resultado = "Reprovado"

print(f"Media: {media}")        
print(f"Resultado: {resultado}")