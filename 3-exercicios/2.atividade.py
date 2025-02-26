import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário um valor e escrever a mensagem: “É MAIOR QUE 10!”.
# Se o valor lido for maior que 10, caso contrário escrever “NÃO É #MAIOR QUE 10!”
# Verifique se o número digitado é igual a 10, caso seja, escreva a mensagem: “O número é igual a 10!”
 
 #solicitando dados
valor = int(input ("Digite um valor: "))

if valor > 10:
    print("É MAIOR QUE DEZ!")
elif valor ==10:
    print (" É IGUAL A DEZ")
else:
    print ("É MENOR QUE DEZ")
print("== FIM ==")

print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")