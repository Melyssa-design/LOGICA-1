// Criando uma lista.
const numero = [1,2,3,4,5]

// Exibindo todos os elementos da lista
console.log("Exibindo elementos da lista")
console.log(numero)

console.log("\nMultiplicação com elementos da lista")
const dobrados = numero.map(n => n * 2)
console.log(dobrados)

console.log("\nFiltrando números pares.")
const pares =  numeros.filter(n => n % 2 === 0)
console.log(pares)

console.log("\nSomando todos os números do vetor.")
const total = numero.reduce((soma, atual) => soma + atual, 0)
console.log(total)