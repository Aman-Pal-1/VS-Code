#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int stack[MAX];
int top = -1;

// Function to push an element onto the stack
void push(int x)
{   
    if (top == MAX - 1)
    {
        printf("Stack overflow\n");
        return;
    }
    stack[++top] = x;
    printf("%d pushed onto the stack\n", x);
}

// Function to pop an element from the stack
int pop()
{
    if (top == -1)
    {
        printf("Stack underflow\n");
        return -1;
    }
    int x = stack[top--];
    return x;
}

// Function to display the stack
void display()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack elements:\n");
    for (int i = top; i >= 0; i--)
    {
        printf("%d\n", stack[i]);
    }
}

int main()
{
    int choice, value;

    while (1)
    {
        printf("\nStack Operations:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter the value to push: ");
            scanf("%d", &value);
            push(value);
            break;
        case 2:
            value = pop();
            if (value != -1)
            {
                printf("%d popped from the stack\n", value);
            }
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
        default:
            printf("Invalid choice\n");
        }
    }

    return 0;
}
