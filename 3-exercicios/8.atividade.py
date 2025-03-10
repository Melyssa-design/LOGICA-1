import os
os.system("clear")

matricula = input("Digite sua matricula: ")
ano = int(input("Digite o ano de seu nascimento: "))
tempo = int(input("Digite seu tempo de trabalho: "))


idade = 2025 - ano

#if idade >= 65 or tempo >= 30:
#   resultado Requerer aposentadoria
# else: 
# print("\nNão requerer")


if idade >= 65:
  print("Requerer aposentadoria")
elif tempo >= 30:
  print("\nRequerer aposentadoria")
else: 
 print("\nNão requerer")

print(f"\nMatricula: {matricula}")
print(f"Tempo: {tempo}")
print(f"Ano: {ano}")


print("\n == QUE A FORÇA ESTEJA COM VOCÊ! == ")