#include <stdio.h>
#include ".\lib\lib.h"

int main() {
    long n = 487221182;

    int factor = polard(n);

    printf("Jeden z faktoru: %d\n", factor);
    printf("Druhý faktor: %d\n", n / factor);

    return 0;
}
