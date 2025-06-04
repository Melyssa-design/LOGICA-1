// FAÇA UM ALGORITIMO QUE LEIA DOIS VALORES INTEIROS A E B SE OS VALORES FOREM IGUAIS
// DEVERA SE SOMAR OS DOIS, CASO CONTARIO DEVERA SE MULTIPLICAR A POR B
// AO FINAL DE QUALQUER UM DOS CALCULOS DEVE-SE ATRIBUIR O RESULTADO PARA UMA VARIAVEL C E MOSTRAR SEU CONTEÚDO NO TERMINAL

const readlineSync = require('readline-sync')

// Lê dois valores inteiros A e B
let pimeiro_numero = parseInt(readlineSync.question("Digite um numero: "))
let segundo_numero = parseInt(readlineSync.question("Digite outro numero: "))

// Verifica se os valores são iguais
let resultado;
if (pimeiro_numero == segundo_numero) {
    resultado = primeiro_numero + segundo_numero
}
