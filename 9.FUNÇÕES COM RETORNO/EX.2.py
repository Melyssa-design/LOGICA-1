import os
os.system ("cls | clear")

#FAZER UM PROGRAM QUE SOLICTE O PREÇO DE UM PRODUTO E INFlACIONE ESSE PREÇO EM 10% 
# SE ELE FOR MENOR QUE 100 E 20% SE ELE FOR MAIOR OU IGUAL A 100
#ULTILIZE UMA FUNÇÃO COM RETORNO PARA OBTER O RESULTADO SOLICITADO


def inflacionar (preco):
    if preco < 100:
        resultado = preco * 1.10
    else:
        resultado = preco * 1.20
    return resultado
 
def desconto (preco):
    if preco < 100:
        desconto = preco * 0.10
    else:
        desconto = preco* 0.20
        return desconto
 

preco_produto = float(input("Digite o preço do produto: "))
preco_inflacionado = inflacionar(preco_produto)
preco_desconto = desconto(preco_produto)

print(f"Preço com inflação: {preco_inflacionado: .2f}")
print(f"Desconto: {preco_desconto}")
