// Criando uma função

function somar(a,b) {
    return a + b
}

function subtrair(a,b) {
    return a - b
}

function multiplicar(a,b) {
    return a * b
}

function dividir(a,b) {
    if (b === 0) {
        return "Divisão por zero não é permitida"
    }
    return a / b
}

// chamando a função
// Adicionar o resultado da função na constante
const soma = somar(2,3)
const subtracao = subtrair(2,3)
const multiplicacao = multiplicar(2,3)
const divisao = dividir(2,3) 
// Mostrar o conteodo da constante
console.log("Soma: ${soma}")
console.log("Subtração: ${subtracao}")
console.log("Multiplicação: ${multiplicacao}")
console.log("Divisão: ${divisao}")

