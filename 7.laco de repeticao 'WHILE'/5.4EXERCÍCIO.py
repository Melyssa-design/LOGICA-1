import os
os.system("cls | clear")
#Crie um programa que solicite ao usuário seu login e uma senha. 
#O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 
#O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, 
# o programa deve ser finalizado.

login_cadastrado = "honey"
senha_cadastrada = "1234"



for i in range (3):
      login = int(input("Digite seu login: "))
      senha = int(input("Digite sua senha: "))

      if login_cadastrado == login and senha_cadastrada == senha:
        print("Acesso permitido")
      else:
        print("Acesso negado.\n")
if i ==3: 
    print("Numeros de tentativas acima do permitido") 