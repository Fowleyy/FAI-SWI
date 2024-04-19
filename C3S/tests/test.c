#include "tap.c"
#include "..\lib\lib.h"

int main(){

    Node kul1, kul2, kul3, kul4;

    kul4.data = 4;
    kul4.next = &kul3;

    kul3.data = 3;
    kul3.next = &kul2;

    kul2.data = 2;
    kul2.next = &kul1;

    kul1.data = 1;
    kul1.next = NULL;

    vypisSeznam(&kul4);

    int result = take_nth(&kul4, 2);
    printf("\n");
    ok(result == 2, "test funkce"); 

    done_testing();

    

}