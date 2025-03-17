import os
os.system("clear")

dia = input("Digite um numero para um dia da semana: ")

match dia: 
  case "1":
     print("Domingo, fim de semama")
  case "2":
     print("Segunda-Feira, dia útil")
  case "3":
     print("Terça-feira, dia útil")
  case "4":
     print("Quarta-Feira, dia útil")
  case "5":
     print("Quinta-Feira, dia útil")
  case "6":
     print("Sexta-Feira, dia útil")
  case "7":
     print("Sábado, fim de semana")

  case _:
    print("iválido!")    

print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")