// Crie um vetor que contenha 6 números, informe quantos são
// pares e quantos são ímpares.

const readlineSync = require('readline-sync')

listaDeNumeros = []

for (let i = 1; i <= 6; i++) {
    numero = readlineSync.question(`Digite o ${i}º número: `)
    listaDeNumeros.push(numero);
}

console.log("\nNumeros pares: ");
const pares = listaDeNumeros.filter(n => n % 2 === 0);
console.log(pares)

console.log("\nNumeros impares:");
const impares = listaDeNumeros.filter(n => n % 2 !== 0);
console.log(impares)