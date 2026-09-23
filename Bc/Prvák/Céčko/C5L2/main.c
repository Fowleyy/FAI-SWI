#include <stdio.h>

typedef struct Node {
    float data;         
    struct Node* next; 
} Node;


float newton_run(int times, Node* zelva, Node* zajic){
    if(times == 0) return 0;

    printf("times - %d\n", times);
    printf("val - %f\n", zelva->data);

    if(zelva->data == zajic->data) {
        printf("Konec\n");
        return zelva->data;

    } else {
        return newton_run(times - 1, zelva->next, zajic->next->next);    
    }
}


int main() {

    Node kul1, kul2, kul3, kul4;

    kul4.data = 4;
    kul4.next = &kul3;

    kul3.data = 3;
    kul3.next = &kul2;

    kul2.data = 2;
    kul2.next = &kul1;

    kul1.data = 1;
    kul1.next = &kul4;

    newton_run(1000, &kul1, &kul4);

    return 0;
}
