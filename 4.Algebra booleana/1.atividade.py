import os
os.system("clear")

#Elabore um algoritmo para solicitar ao usuário o login e a senha.
#Considere que os dados do usuário já estão cadastrados.
#Caso o login e senha estejam corretos, mostre a mensagem:
 #“Bem-vindo!”
#Caso contrário, mostre a mensagem: 
#“Login ou senha inválidos.”

login_cadastrado = "honey"
senha_cadastrada = "1234"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
if login == login_cadastrado and senha == senha_cadastrada:
  print("Seja bem vindo")
else:
  print("Login ou senha inválidos")

  print("\n ==QUE A FORÇA ESTEJA COM VOCÊ== ")