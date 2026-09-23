#include <stdio.h>

int main(){
    int arr[] = {1,2,3,4};

    //printf("%ld", sizeof(arr));

    for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++){
        printf("%d", arr[i]);
    }

    int *valB = arr+1;

    printf("\narr je: %d\n", *valB);
    printf("arr[0] je: %d\n", arr[1]);

    return 0;
}