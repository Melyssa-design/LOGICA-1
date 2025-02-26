import os
os.system("clear")

#Elabore um algoritmo usando operações lógicas para solicitar ao
#usuário 2 números e escrever:
#Os 2 números informados.
# maior número;
#O menor número;

primeiro_numero = int(input("Digite o primeiro numero: "  ))
segundo_numero = int(input("Digite o segundo numero: " ))

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Primeiro numero: {primeiro_numero}")
print(f"Segundo numero: { segundo_numero}")

print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")