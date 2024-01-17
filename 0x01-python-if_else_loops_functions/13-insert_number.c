#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node;
    listint_t *current;

    if (!(new_node = (listint_t *)malloc(sizeof(listint_t)))) {
        return NULL;  /* Allocation failed */
    }

    new_node->data = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    current = *head;
    
    while (current->next != NULL && current->next->data < number) {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}



