import os
os.system ("cls")

forma_de_pagamento = int(input(""" 
1 - A vista
2 - Cartão de credito
Digite a forma de pagamento: """))

valor_produto = float(input("Digite o valor do produto: "))
desconto = 0
acrecimo = 0
match forma_de_pagamento:
    case 1:
        # Aplicando desconto de 10%.
        desconto = valor_produto * 0.10
        valor_pagar = valor_produto - desconto
    case 2:
        acrecimo = valor_produto * 0.10
        valor_pagar = valor_produto + acrecimo

print(f"desconto:{desconto}")
print(f"acrecimo: {acrecimo}")    
print(f"Total: {valor_pagar}")
    