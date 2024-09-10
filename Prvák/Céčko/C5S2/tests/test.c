#include "tap.c"
#include "..\lib\lib.h"


int main() {

    int n = 1189;

    int factor = polard(n);

    ok(factor == 41, "Test - první faktor");

    ok(n / factor == 29, "Test - Druhý faktor");

   

    done_testing();
    return 0;
}