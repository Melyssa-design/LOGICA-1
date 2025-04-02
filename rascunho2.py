import os

os.system("cls | clear")


quantidade_de_pratos = 7
soma = 0
acrescimo = 0
desconto = 0
pratos_escolhidos = " "

print("""
    ============Menu============
    codigo  menu \t    valor
    1- \t   Picanha \t    25,00
    2- \t   Lasanha \t    20,00
    3- \t   Strogonoff \t    18,00
    4- \t   Feijoada\t    16,00
    5- \t   Bife acebolado   15,00
    6- \tFrango a parmegiana 10,00
    7- \t   Pão com ovo\t    5,00 
    """)
  
while True:
    menu = int(input("Escolha o código do prato que deseja: "))
    match menu :
        case 1:
            prato = "1- Picanha|"
            preco = 25.00
        case 2:
            prato = "2- Lasanha|"
            preco = 20.00
        case 3:
            prato = "3- Strogonoff|"
            preco = 18.00
        case 4:
            prato = "4- Feijoada|"
            preco = 16.00
        case 5:
            prato = "5- Bife acebolado|"
            preco = 15.00
        case 6:
            prato = "6- Frago a parmegiana|"
            preco = 10.00
        case 7:
            prato = "7- Pão com ovo|"
            preco = 5.00
        case 0:    
          break
        case _:
            print("Código inválido!")
            print("Digite um código válido: ")
            prato = " "
            preco = 0

    pratos_escolhidos += prato + " "
    soma += preco

    continuar = input("Deseja escolher outro prato? 1- Sim | 0- Não: ").lower()
    if continuar == "0":
        break
print(f"Subtotal: R${soma}")

forma_de_pagamento = int(input(""" 
1 - A vista
2 - Cartão de credito
Digite a forma de pagamento: """))

match forma_de_pagamento:
    case 1:
        desconto = soma * 0.10
        valor_pagar = soma - desconto

        print(f"\nCódigos e pratos escolhidos: {pratos_escolhidos}")
        print(f"Subtotal: R${soma}")
        print(f"Forma de pagamento escolhida: À vista")
        print(f"Valor do desconto: R${desconto: .2f}")
        print(f"Valor final a ser pago: R${valor_pagar: .2f}")
    case 2:
        acrescimo = soma * 0.10
        valor_pagar = soma + acrescimo

        print(f"\nCódigos e pratos escolhidos: {pratos_escolhidos}")
        print(f"Subtotal: R${soma}")
        print(f"Forma de pagamento escolhida: Cartão de crédito")
        print(f"Acréscimo aplicado: R${acrescimo: .2f}")
        print(f"Valor final a ser pago: R${valor_pagar: .2f}")