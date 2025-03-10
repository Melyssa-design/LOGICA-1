import os
os.system("clear")

nome = input("Didite seu nome: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota)/2

#match media:
#    case 1:
#      media >= 9
#      print("A|Aprovado")
#    case 2:
#      media >= 7.5 < 9
#      print("B|Aprovado")
#    case 3:
#      media >= 6 < 7.5
#      print("C|Aprovado")
#    case 4:
#      media >= 4 < 6
#      print("D|Reprovado")
#    case 5:
#      media < 4
#      print("E|Reprovado")
#    case _:
#      print("Inválido")  
 
if media >= 9:
  (print("\nConceito A| Aprovado"))
elif media >= 7.5 < 9: 
  (print("\nConceito B| Aprovado"))
elif media >= 6 < 7.5:
  (print("\nConceito Nota C| Aprovado"))
elif media >= 4 < 6:
  print(print("\nConceito Nota D| Reprovado"))
elif media < 4:
  print ("\nConceito Nota E| reprovado")



print(f"Media: {media}")


print("\n == QUE A FORÇA ESTEJA COM VOCÊ! == ")