import os
os.system("clear")

#ENTRADA
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite Segundo numero: "))
operador = input("Digite a operação desejada (+ - * /): ")

#PROCESSAMENTO
 
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":   
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero

    case _:
     print("opção invalida")

#SAIDA

print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Operador: {operador}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")

print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")