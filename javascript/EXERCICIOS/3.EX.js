// ELABORE UM ALGORITIMO USANDO OPERAÇÕES LÓGICAS PARA INFORMAR SE UMA PESSOA É OBRIGADA A VOTAR.
// CONSIDE QUE A REGRA É:
// MENORES DE 16, NÃO PODEM VOTAR
// ENTRE 16 E 17 ANOS, VOTO OPCIONAL
// A PARTIR DE 18 ANOS, VOTO OBRIGATÓRIO
// MAIORES QUE 65 NÃO SÃO OBRIGADOS A VOTAR


const idade = 60 // Altere este valor para testar diferentes idades
    if (idade < 16) {
        console.log("Não pode votar.");
    } else if (idade == 16 || idade == 17) {
        console.log("Voto opcional.");
    } else if (idade == 18 || idade > 65) {
        console.log("Voto obrigatório.");
    } else (idade >= 65) 
    {   console.log("Não é obrigado a votar.")
}
