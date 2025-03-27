// WAP to implement the following operation on array . insertion

#include <stdio.h>

int main() {
    int arr[100], size, pos;

    printf("Enter the size of the array: ");
    scanf("%d", &size);
    printf("Enter the elements of the array: "); 
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Enter the position to insert: ");
    scanf("%d", &pos);
    for (int i = size; i >= pos; i--) {
        arr[i] = arr[i - 1];
    }
     printf("Enter the element to insert; ");
     scanf("%d", &arr[pos]);
     size++;
        printf("Updated array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
  
