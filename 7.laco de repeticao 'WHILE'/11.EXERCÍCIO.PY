import os
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
#O final da leitura de dados se dará com quando o usuário digitar o número código 3. 
#Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.

soma = 0
media_salarial =0
contador = 0
maior_idade = 0
menor_idade =0
mulheres_com_maior_salario = 0
salario = 0

while True:
    dados = input(""" ~~~~~~~MENU~~~~~~~
Código  |   Descrição
1       |   Adicionar pessoa
2       |   Exibir resultados
3       |   Sair:\n""") 

    match dados:
        case "1":
         print = idade = input(f"Digite sua idade :")
         print = sexo = input("Digite seu sexo: ")
         print = salario = input("Digite seu salario: ") 
         contador +=1
         os.system("cls | clear") 
         if mulheres_com_maior_salario == "f" and salario >= 5000:
           contador+=1
         if maior_idade >=18:
          contador +=1
         elif menor_idade <=17: 
           contador+=1
        
        case "2":
          print(f"Media salarial: {media_salarial}")
          print(f"Menor dade: {menor_idade}")
          print(f"Maior dade: {maior_idade}")
          print(f"Sexo: {sexo}")
          print(f"Salario: {salario}")
          print(f"Qantidade de mulheres com maior faixa salaria{mulheres_com_maior_salario}")
        case "3":
          break
soma += salario
media_salarial = soma/contador