import os 
os.system ("cls || clear")

#CRIANDO LISTA
lista_notas = []

#ADICIONANDO 3 NOTAS EM UMA LISTA.
for i in range (3):
    nota = float(input("Digite uma nota : "))
    lista_notas.append(nota)

#Eximbindo todos os valores em uma lista.
print()
for nota in lista_notas: # ForEach
    print(nota)