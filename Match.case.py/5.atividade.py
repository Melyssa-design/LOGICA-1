import os
os.system("clear")

mes = input("Digite um numéro para um mês: ")


match mes:
  case "1":
    print("Mês selecionado: Janeiro")
  case "2":
    print("Mês selecionado: Fevereiro")
  case "3":
    print("Mês selecionado: Março")
  case "4":
    print("Mês selecionado: Abril")
  case "5":
    print("Mês selecionado: Maio")
  case "6":
    print("Mês selecionado: Junho")
  case "7":
    print("Mês selecionado: Julho")
  case "8":
    print("Mês selecionado: Agosto")
  case "9":
    print("Mês selecionado: Setembro")
  case "10":
    print("Mês selecionado: Outubro")
  case "11":
    print("Mês selecionado: Novembro")
  case "12":
    print("Mês selecionado: Dezembro")

  case _:
    print("Inválido")

print("\n == QUE A FORÇA ESTEJA COM VOCÊ! == ")