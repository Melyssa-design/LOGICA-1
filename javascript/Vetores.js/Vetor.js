// Criando um vetor

const frutas = ["Maçã", "Banana", "Laranja"]

console.log("exibindo todos os elementos do vetor")
console.log(frutas)

console.log("\nExibindo apenas um elemento dentro do vetor. ")
console.log(frutas[0])
console.log(frutas[2])

console.log("\nAdicionadno o elemento ao vetor")
frutas.push("Uva")
console.log(frutas)

console.log("\nRemovendo o último elemento do vetor")
frutas.pop()
console.log(frutas)

console.log("\nRemovendo o primeiro elemento do vetor")
frutas.shift()
console.log(frutas)

console.log("\npercorrendo o vetor")
frutas.forEach((fruta, index) => {
    console.log(`${++index}: ${fruta}`)
})
// for (let i = 1; i <= 5; ++i) {
    // console.log(i)
