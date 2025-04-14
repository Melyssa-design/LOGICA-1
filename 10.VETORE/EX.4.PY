import os 
os.system ("cls || clear")

def calcuar_media(lista):
    return sum(lista_notas) / QUANTIDADE_NOTAS

def verificar_resultado(media):
    if media >= 7:
     resultado = ("Aprovado!")
    elif media >= 5:
     resultado = ("Recuperação")
    else:
     resultado =("Reprovado!")  
    return resultado

#CRIANDO LISTA
lista_notas = []
QUANTIDADE_NOTAS = 4

#ADICIONANDO 3 NOTAS EM UMA LISTA.
for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota : "))
    lista_notas.append(nota)

#calcular meida e verificar
meida  = calcuar_media(lista_notas)
resultado = verificar_resultado(media)
 
#EXIBINDO RESULTADO
print()
for nota in lista_notas:
    print(nota)
print(f"Media: {media}")    
print(f"resultao: {resultado}")