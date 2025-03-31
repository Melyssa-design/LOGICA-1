import os
import time
os.system ("cls | clear")

#Foi feita uma pesquisa entre os habitantes de uma região.  
# Foram coletados os dados de idade, sexo (M/F) e salário. 
#Faça um algoritmo que informe:  
#a) a média de salário do grupo;
#b) maior e menor idade do grupo;
#c) quantidade de mulheres com salário a partir de R$ 5.000,00.
#Crie um menu com três opções.
#Código  |   Descrição
#1       |   Adicionar pessoa
#2       |   Exibir resultados
#3       |   Sair
# O final da leitura de dados se dará com quando o usuário digitar o número código 3. 
#Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.

soma = 0
contador = 0
maior_idade = 0
menor_idade =0
mulheres_com_maior_salario = 0

while True:
    dados = input(""" ~~~~~~MENU~~~~~~~
Código  |   Descrição
1       |   Adicionar pessoa
2       |   Exibir resultados
3       |   Sair:\n""") 

    opção = int(input("Digite uma opção:"))
    
    match opção:
        case "1":
         idade = int(f"Digite sua idade :")
         sexo = input("Digite seu sexo: ")
         salario = float(input("Digite seu salario: ") )
         contador +=1
         soma_salario += salario
         maior_idade = max(maior_idade, idade)
         menor_idade = min(menor_idade, idade)     
         if sexo == "f" and salario >= 5000:
          mulheres_com_maior_salario +=1

         os.system("cls | clear") 
        case "2":
           if contador > 0:
             media_salarial = soma_salario/ contador
             print(f"Media salarial: {media_salarial}")
             print(f"Menor dade: {menor_idade}")
             print(f"Maior dade: {maior_idade}")
             print(f"Qantidade de mulheres com maior faixa salaria: {mulheres_com_maior_salario}")
           else:
             print("\nNão foram informados os dados necessários.")
             time.sleep(3)
             os.sleep("cls | clear")
        case "3":
          print ("\n=FIM=")
          break
        case _:
            print("\nOpção inválida.")
            time.sleep(3)
            os.sleep("cls | clear")

