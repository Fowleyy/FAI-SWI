#include <stdio.h>

int main() {
    char * name = "adam";
    char * othername = name;
    printf("%s\n", name);

    int arr[] = {1,2,3,4};
    int * brr = arr;

    brr[0] = 55;
    printf("%d\n", arr[0]);
    printf("%s\n", othername);

    return 0;
}