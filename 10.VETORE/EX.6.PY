import os
os.system ("cls || clear")

lista_numeros =[]
QUANTIDADE_NUMEROS = 6
pares = 0
impares = 0

print("NUMEROS PARES E ÍMPARES: ")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite O {i+1}° número: "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1
print("\nMostrando resultados")        
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}° número: {numero}")
        
print(f"\nNúmeros pares: {pares}")
print(f"Números impares: {impares}")