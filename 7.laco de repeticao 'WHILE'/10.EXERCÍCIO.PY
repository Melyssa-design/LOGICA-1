import os
os.system ("cls | clear")

#Faça um algoritmo que leia uma quantidade não determinada de números inteiros positivos. 
# Calcule:  quantidade de números pares e ímpares; 
#média de valores pares 
#média geral dos números lidos. 
#O número que encerrará a leitura será o número zero.

media_geral = 0
pares = 0
impares = 0
soma_par = 0
soma_impar= 0
contador = 0
soma_geral = 0

while True: 
    numero = int(input("Digite um numero: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        pares += 1
        soma_par += numero
    else:
        impares +=1
        soma_impar += numero
    
    contador +=1 
    soma_geral += numero

if contador == 0:
        soma = numero
        contador = 1   

media_par = soma_par/ pares
media_impar = soma_impar/impares
media_geral = soma_geral/contador


print()
print(f"Numeros totais: {contador}\n")
print(f"Numeros pares: {pares}")
print(f"Numeros impares {impares}\n")
print(f"Media dos numeros pares: {media_par}")
print(f"Media dos numeros impares: {media_impar}")
print(f"Meida geral: {media_geral}")

