// Crie um vetor com 5 números, mostre a quantidade de
// números negativos e a soma dos números positivos desse vetor.

const readlineSync = require('readline-sync')

listaDeNumeros = []

for (let i = 1; i<= 5; i++) {
    numero = readlineSync.questionInt(`Digite o ${i}º número: `)
    listaDeNumeros.push(numero)
}

console.log("\nNumeros negativos: ")
const negativos = listaDeNumeros.filter(n => n < 0)
console.log(negativos)

console.log("\nQuantidade de números positivos: ")
const positivos = listaDeNumeros.filter(n => n > 0) //.reduce((soma,total) => soma + total, 0)
console.log(positivos)

console.log("\nSoma dos números positivos:")
const somaPositivos = positivos.reduce((soma,total) => soma + total, 0)
console.log(somaPositivos)
