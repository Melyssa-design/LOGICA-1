// Crie um vetor com 3 notas, calcule a média aritmética.
// Mostre as 3 notas e informe a média.

const readlineSync = require('readline-sync')

listaDeNotas =[]
for (let i = 1; i <= 3; i++) {
    nota = readlineSync.question('Digite a ${i}ª nota')
    listaDeNotas.push(nota)
}
console.log("\nSoma das notas: ")
soma = listaDeNotas.reduce((soma, atual) => soma + atual, 0)
console.log(soma)

console.log("\nQuantidade de notas: ")
qauntidadeDeNotas = listaDeNotas.length
console.log

console.log('\nMedia:')
media = soma / qantidadeDeNotas
console.log(meida)

console.log("\nExibindo Notas: ")
listaDeNotas.forEach((nota, index) => console.log(`${++index}ª nota: ${nota} `))