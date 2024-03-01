#include "tap.c"
#include "..\lib\mymath.h"

int main() {


    ok(faktorial(5) == 120, "test faktorial");
    ok(mocnina(2,2) == 4, "test mocnina");


    done_testing();

    
    
}


