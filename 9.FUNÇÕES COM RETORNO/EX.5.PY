import os
os.system ("cls | clear")


soma = 0
media = 0
def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma/2
    return media

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado.")

media = calcular_media(primeira_nota,segunda_nota)

print(f"Media: {media}")