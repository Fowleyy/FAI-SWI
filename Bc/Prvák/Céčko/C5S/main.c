#include <stdio.h>
#include <math.h>

long naive(long n, long start) {
    if(n % start == 0) {
        return start;
    }
    return naive(n, start-1);
}

int main()
{    
    printf("%ld", naive(103*103, sqrt(103*103)));
    return 0;
}   