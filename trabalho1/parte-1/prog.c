#include <stdio.h>

// Função para somar os itens de um array de doubles
double somaArray(double array[], int n) {
    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        soma += array[i];
    }
    return soma;
}

// Função para calcular a média dos itens de um array com elementos double float
double mediaArray(double array[], int n) {
    if (n == 0) {
        return 0.0; // Evitando divisão por zero
    }

    double soma = somaArray(array, n);
    return soma / n;
}

// Função para encontrar o maior item em um array com elementos double float
double maiorElementoArray(double array[], int n) {
    if (n == 0) {
        return 0.0; // Array vazio
    }

    double maior = array[0];
    for (int i = 1; i < n; i++) {
        if (array[i] > maior) {
            maior = array[i];
        }
    }
    return maior;
}

int main() {
    int n;

    // Aqui o usuário vai fornecer o número de elementos do array com elementos double float
    printf("Digite o número de elementos no array: ");
    scanf("%d", &n);

    // Cria um array com elementos double float do tamanho especificado
    double array[n];

    // Preencher o array com valores fornecidos pelo usuário 
    // Não temos condição para erro de digitação
    printf("Digite os elementos do array:\n");
    for (int i = 0; i < n; i++) {
        scanf("%lf", &array[i]);
    }

    // Request para as 3 funções e print do resultado
    printf("Soma dos elementos: %.2lf\n", somaArray(array, n));
    printf("Média dos elementos: %.2lf\n", mediaArray(array, n));
    printf("Maior elemento: %.2lf\n", maiorElementoArray(array, n));

    return 0;
}
