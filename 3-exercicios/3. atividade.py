import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário três notas.
# Caso a média do aluno seja menor que 7, o aluno está reprovado. 
# Mostrar: média e se está aprovado ou reprovado.

#solicitando dados
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota =float(input("Digite a terceira nota: "))


soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print(f"Média: {media}")

if media < 7:
    print("REPROVADO. ")
else:
    print('APROVADO.')
