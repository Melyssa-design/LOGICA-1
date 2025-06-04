// Crie um vetor com 3 notas, calcule a média aritmética.
// Mostre as 3 notas e informe a média.

const numero = [7,6,9]

console.log("Exibindo notas")
const soma = numero.reduce((soma, atual) => soma + atual, 0)
console.log(numero)
console.log(`A média é: ${soma / numero.length}`)
