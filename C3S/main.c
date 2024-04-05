#include <stdio.h>
#include ".\tests\tap.c"
  
typedef struct Node {
    int data;         
    struct Node* next; 
} Node;


int vypisSeznam(Node* node) {
    if (node == NULL) {
        printf("NULL\n");
        return 0;

    }
    printf("%d -> ", node->data);
    vypisSeznam(node->next);
}


int take_nth(Node* node, int p) {
  if (node == NULL) {
    printf("NULL\n");
    return 0;
  }

  if (p == 0) {
    printf("%d", node->data);
    return node->data;
  }

  take_nth(node->next, p - 1);
}

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

    

    int result = take_nth(&kul4, 2);
    printf("\n");
    ok(result == 2, "test funkce"); 

    done_testing();

}


