import os
os.system("clear")

#FAÇA UMA PROGRAMA QUE CALCULE O "PESO IDEAL" DE UMM USUÁRIO DE ACORDO COM UM CARACTERE IDENTIFICADOR DE SEXO ("M" PAA MASCULINO OU "F" PARA FEMININO) INSERINDO PELO MESMO. A FÓRMULA PARA CASA UM DOS DOIS CASOS ESTA DEFINIDA ABAIXO.
#CASO "M", UTILIZE A FORMULA:
#(72. X ALTURA) - 58
#CASO "F", ULTILIZE A FORMULA: (62.1 X ALTURA) - 44.7


altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

match sexo:
  case "M" | "m":
    peso_ideal = (72.7 * altura) - 58
    print(f"\nPeso ideal: {peso_ideal}")
  case "F" | "f":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"\nPeso ideal: {peso_ideal}")
  case _:
    print("opção invalida.")

print("\n == QUE A FORÇA ESTEJA COM VOCÊ! == ")
