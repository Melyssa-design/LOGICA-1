import os
os.system("clear")

nome = input("Didite seu nome: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota)/2
nota = float
match nota:
    case 1:
      nota = (media >= 9)
      print("Nota A|Aprovado")
    case 2:
      nota = (media >= 7.5 < 9)
      print("Nota B|Aprovado")
    case 3:
      nota  = (media >= 6 < 7.5)
      print("Nota C|Aprovado")
    case 4:
      nota  = (media >= 4 < 6)
      print("Nota D|Reprovado")
    case 5:
       nota = (media < 4)
       print("Nota E|Reprovado")
    case _:
      print("Inválido")  


print(f"Primeiro nota: {primeira_nota}")
print(f"Segundo nota: { segunda_nota}")
print(f"Media: {media}")