import os
os.system("clear")

# Elabore um algoritmo para receber dois inteiros como entrada do teclado e escreva na tela: 
# A média, a soma, o produto, o menor valor e o maior valor.
# Além disso, verifique se os números informados pelo usuário são iguais.
# Usando uma linha para cada resultado.

#solicitando dados

primeiro_numero = int(input("Digite o valor do Primeiro numero: "))
segundo_numero = int(input("Digite o valor do Segundo numero: "))


media = (primeiro_numero + segundo_numero)/2
produto = primeiro_numero * segundo_numero


menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print("\nExibindo resultado: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")

if primeiro_numero == segundo_numero:
    print ("Os numeros são iguais.")
else: 
     print(f"Menor: {menor}")
     print(f"Maior: {maior}")