import os 
os.system ("cls || clear")

#CRIANDO LISTA
lista_notas = []
QUANTIDADE_NOTAS = 4

#ADICIONANDO 3 NOTAS EM UMA LISTA.
for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota : "))
    lista_notas.append(nota)
    

#SOMA E MEDIA
media = sum(lista_notas) /QUANTIDADE_NOTAS

if media >= 7:
  resultado = ("Aprovado!")
elif media >= 5:
    resultado = ("Recuperação")
else:
   resultado =("Reprovado!")   

 

#EXIBINDO RESULTADO
print()
for nota in lista_notas:
    print(nota)
print(f"Media: {media}")    
print(f"resultao: {resultado}")