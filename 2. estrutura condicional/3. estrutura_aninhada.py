import os
os.system("clear")

idade = 17

# se idade < 12 entao
#    escreval ("acesso negado")
# senao se idade < 18 então
#    escreval (" Somente com permisão dos pais.")
# fimse

if idade < 12: # condicional simple
    print("Acesso negado. ")
elif idade < 18: # possibilidade a mais( colocar quando ter 3 ou mais possibilidades)
    print("Somente com permisão dos pais. ")
else: 
    print ("Acesso permitido")    

print("== FIM ==")

