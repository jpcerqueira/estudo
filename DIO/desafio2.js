function registrarResultado(vitorias, derrotas) {
    const saldoVitorias = vitorias - derrotas;
    let nivel = '';

    // Estruturas de decisão para determinar o nível
    if (saldoVitorias < 10) {
        nivel = 'Ferro';
    } else if (saldoVitorias >= 11 && saldoVitorias <= 20) {
        nivel = 'Bronze';
    } else if (saldoVitorias >= 21 && saldoVitorias <= 50) {
        nivel = 'Prata';
    } else if (saldoVitorias >= 51 && saldoVitorias <= 80) {
        nivel = 'Ouro';
    } else if (saldoVitorias >= 81 && saldoVitorias <= 90) {
        nivel = 'Diamante';
    } else if (saldoVitorias >= 91 && saldoVitorias <= 100) {
        nivel = 'Lendário';
    } else if (saldoVitorias >= 101) {
        nivel = 'Imortal';
    }

    return `O Herói tem de saldo de ${saldoVitorias} e está no nível ${nivel}.`;
}

// Teste com valores definidos
const vitorias = 0;
const derrotas = 0;
const resultado = registrarResultado(vitorias, derrotas);
console.log(resultado);