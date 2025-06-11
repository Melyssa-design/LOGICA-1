function gerarTabuada() {
    // <!-- Pegar o valor input do HTML. -->
    const numeroInput = document.getElementById('numeroInput');
    let numero = parseInt(numeroInput.value)

    //  mostra o resultado onde a tabela deve ser exibida. 
    const resultadoDiv = document.getElementById('resultadoTabuada')
    resultadoDiv.innerHTML = ''

    // <!-- Adicionar um titulo para a tabuada -->
    resultadoDiv.innerHTML = `<h2>Tabuada do ${numero}</h2>`

    // Laço de repetição para gerar a tabuada.
    for (let i = 1; i <= 10; i++) {
        const resultado = numero * i;
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`;
    }

}

// a função gerarTabuada sera executada quando o botão for clicado.
const botaoGerar = document.getElementById('gerarTabuada');
botaoGerar.addEventListener('click', gerarTabuada);