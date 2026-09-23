#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    int * arr;
    int length;

}Vector;

void push(Vector * old, int item) {
    if(old->length == 0){
        int * newkus = malloc(sizeof(item));
        newkus[0] = item;
        old ->arr = newkus;
        old ->length = 1;

    } else {
        realloc(old->arr,sizeof(int)*old->length+sizeof(int));
        old->arr[old->length++] = item;
        old->length++;

    }
}

int * insert(int * old, size_t oldsize, int item){
    //prevzit stare pole

    //vytvorit nove
    size_t newsize = oldsize + sizeof(item);
    int * newarr = (int*)malloc(newsize);
    //zkopirovat prvky stareho
    memcpy(newarr, old, oldsize);
    //nakonec vratit nový item
    newarr[(newsize/sizeof(item))-1] = item;

    //vratit nove

    return newarr;
}

void PrintArr(int *old, int length) {
    if (length == 0) {
        return;
    }
    PrintArr(old, length -1);
    printf("%d", old[length-1]);

}

int main() {

    int arr[10];

    int size = 10*sizeof(int);

    malloc(size);

    int * halda = malloc(size);

    halda[0] = 1;
    halda[1] = 2;
    halda[2] = 3;

    //PrintArr(halda, size/sizeof(int));
    int * nove = insert(halda, size, 5);
    /*printf("nove:\n");
    PrintArr(nove, size/sizeof(int)+1);
    printf("stare:\n");
    PrintArr(halda, size/sizeof(int));*/

    Vector vec = {NULL, 0};
    push(&vec, 2);
    push(&vec, 3);
    push(&vec, 5);

    PrintArr(vec.arr, vec.length);

    free(nove);
    free(halda);
    free(vec.arr);
}