import os 
os.system ("cls || clear")

#CRIANDO LISTA
lista_notas = []
#QUANTIDDADE_NOTAS = 3

#ADICIONANDO 3 NOTAS EM UMA LISTA.
for i in range (3):# for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota : "))
    lista_notas.append(nota)

#SOMA E MEDIA
soma = sum(lista_notas)  #media = sum(lista_notas) /QUANTIDADE_NOTAS
media =  soma / 3

#EXIBINDO RESULTADO
print()
for nota in lista_notas:
    print(nota)
print(f"Media: {media}")    