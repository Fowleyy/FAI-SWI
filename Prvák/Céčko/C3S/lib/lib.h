#include <stdio.h>

  
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