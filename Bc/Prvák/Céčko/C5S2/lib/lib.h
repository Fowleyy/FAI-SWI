#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}


int f(int x, int c, int n) {
    return (x * x + c) % n;
}


int polard(int n) {
    int zelva = rand() % n;
    int zajic = zelva;
    int d = 1;

    while (d == 1) {
        zelva = f(zelva, 1, n);
        zajic = f(f(zajic, 1, n), 1, n);
        d = gcd(abs(zelva - zajic), n);
    }

    return d;
}