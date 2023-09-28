#include <stdio.h>
#include "soma.h"
#include "media.h"
#include "maior.h"

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
