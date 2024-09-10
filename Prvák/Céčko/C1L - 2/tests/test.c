#include "tap.c"
#include "..\lib\mathlib.c"

int main() {

    ok(add(5,6) == 1, "test add");
    done_testing();
}