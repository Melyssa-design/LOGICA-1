import os
os.system ("clear")

lista_pedidos = []
precos_pratos = []


def soma_prato(opcao):
  soma += preco
while True:
 
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
      preco = 25
     case 2:
      print("Lasanha \t R$ 20,00 ")
      preco = 20
     case 3:
      print("Strogonoff \t R$ 18,00 ")
      preco = 18
     case 4:
      print("Bife acebolado\t R$ 15,00 ")
      preco = 15
     case 5:
      print("Pão com ovo \t R$ 5,00")
      preco = 5
     case _:
      print("opção invalida")
      preco = 0
      soma += preco
      
 if opcao >= 1 and opcao <= 5:     
  lista_pedidos.append(opcao)
  precos_pratos.append(preco)

 continuar = input("Deseja escolher outro prato\nDigite 'Sim' ou 'Não': ").lower()
 if continuar == "n":
      break

print ("\nPRATO ESCOLHIDO")
for prato in lista_pedidos:
  print (f"Prato: {prato}")
print (f"\nTotal: {sum(precos_pratos)}")