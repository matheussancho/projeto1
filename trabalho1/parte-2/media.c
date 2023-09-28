/* Arquivo que vai fazer a média dos números da array: media.c */
#include <stdio.h>

double mediaArray(double array[], int n) {
    if (n == 0) {
        return 0.0; // Evitando divisão por zero
    }

    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        soma += array[i];
    }
    return soma / n;
}
