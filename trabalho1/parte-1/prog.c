#include <stdio.h>

// Função para somar os elementos de um array de doubles
double somaArray(double array[], int n) {
    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        soma += array[i];
    }
    return soma;
}

// Função para calcular a média dos elementos de um array de doubles
double mediaArray(double array[], int n) {
    if (n == 0) {
        return 0.0; // Evitando divisão por zero
    }

    double soma = somaArray(array, n);
    return soma / n;
}

// Função para encontrar o maior elemento em um array de doubles
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

    // Solicitar o número de elementos ao usuário
    printf("Digite o número de elementos no array: ");
    scanf("%d", &n);

    // Criar um array de doubles com o tamanho especificado
    double array[n];

    // Preencher o array com valores fornecidos pelo usuário
    printf("Digite os elementos do array:\n");
    for (int i = 0; i < n; i++) {
        scanf("%lf", &array[i]);
    }

    // Chamar e imprimir os resultados das três funções
    printf("Soma dos elementos: %.2lf\n", somaArray(array, n));
    printf("Média dos elementos: %.2lf\n", mediaArray(array, n));
    printf("Maior elemento: %.2lf\n", maiorElementoArray(array, n));

    return 0;
}
