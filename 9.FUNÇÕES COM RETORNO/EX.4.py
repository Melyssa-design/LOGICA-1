import os
os.system ("cls | clear")

soma = 0

def calcular_media(nota):
    media = soma/3
    return media

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota 

media = calcular_media(nota)

print(f"Media: {media}")

#def calcular(n1,n2):
# soma = n1 + n2
#