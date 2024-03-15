#include <stdio.h>

int sum_n(int n){
    if (n < 0) {
        return 0;
        }
    else 
    {
        return (n + sum_n(n - 1));
    }
}