/* Arquivo que vai somar os números da array: soma.c */
#include <stdio.h>

double somaArray(double array[], int n) {
    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        soma += array[i];
    }
    return soma;
}
