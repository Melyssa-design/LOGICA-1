import os
os.system("cls | clear")

#Escreva um algoritmo que solicite ao usuário 5 valores
#inteiros e ao final mostre: 
#a-quantos números são pares; 
#b-quantos números são ímpares;

pares = 0
impares = 0
print("NUMEROS PARES E ÍMPARES: ")
for i in range(5):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1
print()
print (f"Pares {pares}")
print (f"Imares {impares}")
