#include "tap.c"
#include "..\lib\vector.h"


int main() {

    Vector *vector = Vector_create();

    vector = Vector_insert(vector, 10);
    ok(vector->data[0] == 10, "Test - Insert");

    int static_array[] = {1, 2, 3};
    vector = from_static(static_array, 3);
    ok(vector->data[0] == 1 && vector->data[1] == 2 && vector->data[2] == 3, "Test - from_static");

    vector = Vector_delete_at(vector, 1);
    ok(vector->data[0] == 1 && vector->data[1] == 3, "Test - Delete at");

    vector = vector_sort(vector, 1);
    ok(vector->data[0] == 1 && vector->data[1] == 3, "Test - Ascending");

    vector = vector_sort(vector, 0);
    ok(vector->data[0] == 3 && vector->data[1] == 1, "Test - descending");

    done_testing();
    return 0;
}