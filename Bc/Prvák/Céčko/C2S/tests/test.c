#include "tap.c"
#include "..\lib\mymath.h"

int main() {

    Result result = scitani(5, 6);

    result = faktorial(5);
    ok(result.vysledek == 120, "test faktorial");


    done_testing();

    
}


