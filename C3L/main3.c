#include <stdio.h>
int arr[] = {1,2,3,4};

void printArrLoop(int *arr, int legth) {
    for(int i = 0; i < legth; i++)
        printf("%d,", arr[i]);
}

void printArrRec(int *arr, int length) {
    if (length <= 0) {
        return;
    } else {
        printf("%d,", *arr);
        printArrRec(arr + 1, length - 1);
    }
}



int main() {
    
    printArrLoop(arr, 4);
    printf("\n");
    printArrRec(arr, 4);
}