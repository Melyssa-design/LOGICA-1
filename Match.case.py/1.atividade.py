import os
os.system("clear")

dia = input("Digite um dia da semana: ")

match dia: 
 case "segunda":
     print("Hoje é segunda-feira.")
 case "terça":
     print("Hoje é terça-feira.")
 case "quarta":
     print("Hoje é quarta-feira.")
 case "quinta":
     print("Hoje é quinta-feira.")
 case "sexta":
     print("Hoje é sexta-feira.")
 case "sabado" | "domingo":
     print("Hoje é fim de semana.")
 case _:
     print("dia inválido.")

print(dia)

print(" ==QUE A FORÇA ESTEJA COM VOCÊ== ")