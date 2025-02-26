import os
os.system("clear")


valor = float(input("Digite o valor do produto: " ))
parcela = int(input("Digite a quantidade de parcelas":))
pagamento = int(input("""Digite a forma de pagamento:
\n1 - A vista:
2 - A prazo: """)) 


match pagamento:
    case 1:
        desconto = valor * 0.1
        print("")
    case 2:

match parcela:
    case   




print(f"Valor do produto: {pagamento}")
print(f"Forma de pagamento: {pagamento}")
print(f"Valor do desconto: {pagamento}")