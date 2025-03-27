// WAP to implement the following operation on array .deletion.

#include <stdio.h>

int main() {
    int arr[100], size, pos;

    printf("Enter the size of the array: ");
    scanf("%d", &size);
    printf("Enter the elements of the array: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the position to delete: ");
    scanf("%d", &pos);

    for (int i = pos; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    size--; 

    printf("Updated array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
