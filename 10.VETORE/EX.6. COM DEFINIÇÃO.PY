import os
os.system ("cls || clear")

lista_numeros =[]
QUANTIDADE_NUMEROS = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
       if numero % 2 == 0:
          pares +=1
       else:
          impares += 1
          return pares, impares
       
print("= Solicitando números =") 
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite O {i+1}° número: "))
    lista_numeros.append(numero)
    
pares, impares = pares_impares(lista_numeros)

print("\nMostrando resultados")        
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}° número: {numero}")
        
print(f"\nNúmeros pares: {pares}")
print(f"Números impares: {impares}")