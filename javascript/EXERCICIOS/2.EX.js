const readlineSync = require ("readline-sync")

soma = 0
let nota  = 0

for (let i=1; i <= 2; i++) { 
    do {
        nota = readlineSync.questionFloat("Digite uma nota: ")
} while (nota < 0 || nota > 10)
    soma += nota
}

media = soma / 2

console.log("A media é: ${meida}")
// print(f"Media: {media}) // Pyrthon
