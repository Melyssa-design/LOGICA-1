import os
os.system("cls | clear")
#Crie um programa que solicite ao usuário seu login e
#uma senha. 
#O programa deve continuar pedindo o login e a senha
#até que ambos estejam corretos.

login_cadastrado = "honey"
senha_cadastrada = "1234"

while True:
    login = int(input("Digite seu login: "))
    senha = int(input("Digite sua senha: "))

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Acesso permitido")
        break
    else:
      print("Acesso negado.\n")
      


