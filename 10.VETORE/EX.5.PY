import os 
os.system ("cls || clear")
import time
#CRIANDO LISTA
lista_numeros = []
QUANTIDADE_NUMEROS = 5
#ADICIONANDO 3 NOTAS EM UMA LISTA.
for i in range (QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}° número : "))
    lista_numeros.append(numero)


menor = min(lista_numeros)
maior = max(lista_numeros)

print("\nMostrandor números")
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}° número: {numero}")
    time.sleep(5)

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")