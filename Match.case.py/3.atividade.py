import os
os.system("clear")

#ENTRADA

opcao = int(input("""Código \t Prato \t\t Valor 
\n1 \t Picanha R$ \t\t 25,00   
2 \t Lasanha R$ \t\t 20,00
3 \t Strogonoff R$ \t\t 18,00                      
4 \t Bife acebolado R$ \t 15,00
5 \t Pão com ovo R$ \t 5,00 
\nDigite a opção desejada: """))

match opcao:
    case 1:
     print("Picanha \t R$ 25,00 ")
    case 2:
     print("Lasanha \t R$ 20,00 ")
    case 3:
     print("Strogonoff \t R$ 18,00 ")
    case 4:
     print("Bife acebolado\t R$ 15,00 ")
    case 5:
     print("Pão com ovo \t R$ 5,00")
       
    case _:
     print("opção invalida")

print(f"Opção: {opcao}")
            

print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")