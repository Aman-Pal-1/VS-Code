#include <stdio.h>

void shift(int arr[], int n) {
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != 0) {
            arr[j++] = arr[i];
        }
    }
    while (j < n) {
        arr[j++] = 0;
    }
}

void print(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {2, 3, 4, 5, 0, 1, 0, 2, 0, 3, 0, 4, 5, 67, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    print(arr, n);
    shift(arr, n);
    print(arr, n);

    return 0;
}