const usuarios = [
    {nome: "Ana", idade: 25},
    {nome: "Marta", idade: 32},
    {nome: "Maria", idade: 45}
]
// EXIBIR NO CONSOLE
console.log("Exibindo todos os elementos do vetor")
usuarios.forEach(usuario => {
console.log(`${usuario.nome} tem ${usuario.idade} anos`)
})

console.log("\nFiltrando usuário.")
console.log("Apenas usuários até 30 anos.")
const menorQueTrintaAnos = usuarios.filter(usuario => usuario.idade <= 30)
menorQueTrintaAnos.forEach(usuario => console.log(`${usuario.nome} tem ${usuario.idade} anos`))

console.log("\nExibindo apenas o nome dos usuários.")
const nome = usuarios.map(usario => usario.nome)
nome.forEach( nome => {
    console.log(`Nome: ${nome}`)

})

console.log("\nExibindo o nome dos usuários com numeração.")
const nomes = usuarios.map(usuario => usuario.nome)
nomes.forEach((nome, index) => {
    console.log(`${++index}: ${nome}`)
})

console.log("\nEncontra um usuário.")
const usuarioEncontrado = usuarios.find(usuario => usuario.nome === "Marta")
console.log(`Nome: ${usuarioEncontrado.nome}, idade: ${usuarioEncontrado.idade}`)

console.log("\nMostrar a soma de todas as idades.")
const somaIdades = usuarios.reduce((total, usuario) => total + usuario.idade, 0)
console.log(`Total: ${somaIdades}`)



// FUNÇOES DA LISTA

// forEach: Executa uma função para cada elemento do vetor.
// filter: Filtra os elementos do vetor com base em uma condição.
// map: Cria um novo vetor com os resultados da aplicação de uma função a cada elemento do vetor.
// find: Encontra um elemento do vetor que atende a uma condição.
// reduce: Reduz o vetor a um único valor, aplicando uma função acumuladora a cada elemento.
// some: Retorna a soma de todos os elementos do vetor.
// every: Verifica se todos os elementos do vetor atendem a uma condição.
// includes: Verifica se um elemento está presente no vetor.
// indexOf: Retorna o índice do primeiro elemento que atende a uma condição.
// lastIndexOf: Retorna o índice do último elemento que atende a uma condição.
// sort: Ordena os elementos do vetor com base em uma função de comparação.
// reverse: Inverte a ordem dos elementos do vetor.
// join: Junta os elementos do vetor em uma string, usando um separador especificado.
// slice: Retorna uma parte do vetor, especificada por um intervalo de índices.
// splice: Adiciona ou remove elementos do vetor em um índice específico.
// concat: Concatena dois ou mais vetores, criando um novo vetor.
// toString: Converte o vetor em uma string, separando os elementos por vírgulas.
// split: Divide uma string em um vetor, usando um separador especificado.