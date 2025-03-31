import os

os.system("cls | clear")


quantidade_de_pratos = 7
soma = 0
acrescimo = 0
desconto = 0
pratos_escolhidos = " "

while True:
    menu = float(input("""
    =========Menu========
    codigo  menu \t    valor
    1- \t   Picanha \t    25,00
    2- \t   Lasanha \t    20,00
    3- \t   Strogonoff \t    18,00
    4- \t   Feijoada\t    16,00
    5- \t   Bife acebolado   15,00
    6- \t   Frango a parmegiana 10,00
    7- \t   Pão com ovo\t    5,00  
    Escolha o prato que deseja:
    """))
  
    match menu :
        case 1:
            prato = "Picanha | codigo 1"
            preco = 25.00
        case 2:
            prato = "Lasanha | codigo 2"
            preco = 20.00
        case 3:
            prato = "Strogonoff | codigo 3"
            preco = 18.00
        case 4:
            prato = "Feijoada | codigo 4"
            preco = 16.00
        case 5:
            prato = "Bife acebolado | codigo 5"
            preco = 15.00
        case 6:
            prato = "Frago a parmegiana | codigo 6"
            preco = 10.00
        case 7:
            prato = "Pão com ovo | codigo 7"
            preco = 5.00
        case 0:    
          break
    pratos_escolhidos += prato + " "

    soma += preco
    continuar = input("""Deseja escolher outro prato? 
    1- Sim
    0- Não digite '0'
    """).lower()
    if continuar == "0":
        break

forma_de_pagamento = int(input(""" 
1 - A vista
2 - Cartão de credito
Digite a forma de pagamento: """))

match forma_de_pagamento:
    case "A vista":
        # Aplicando desconto de 10%.
        desconto = preco * 0.10
        valor_pagar = soma - desconto
    case "cartão":
        acrescimo = preco * 1.1
        valor_pagar = soma + acrescimo

print(f"Subtotal: R${soma}")
print(f"\nPratos escolhidos: {pratos_escolhidos}")
print(f"Forma de pagamento escolhida: {forma_de_pagamento}")
print(f"Valor do desconto: {desconto}")
print(f"Acréscimo aplicado: {acrescimo}")
print(f"Valor final a ser pago: {valor_pagar}")