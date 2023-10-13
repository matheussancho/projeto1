/* Arquivo que vai realizar a comparação entre os números da array: maior.c */
#include <stdio.h>

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
