#include <stdio.h>

int main() {
    int a = 5;

    printf("adress - %p\n", &a);
    printf("velikost - %ld\n", sizeof(a));
    
    int * pA = &a;

    printf("hodnota pa - %p\n", pA);
    printf("adresa pa - %p\n", &pA);

    int * point = NULL;
    point = &point;

    double b = 5.0;

    //printf("%d", 5);

    return 0;
}