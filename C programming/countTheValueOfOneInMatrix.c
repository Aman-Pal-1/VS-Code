#include <stdio.h>

int main()
{
    int arr[3][4] = {{1, 0, 1, 1}, {0, 0, 1, 1}, {1, 0, 1, 0}};
    
    // Display the matrix
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    printf("--------------------------------------------------------\n");

    for (int i = 0; i < 3; i++)
    {
        int sum = 0; 
        printf("Row %d elements: ", i + 1); 

        for (int j = 0; j < 4; j++)
        {
            printf("%d ", arr[i][j]);
            sum += arr[i][j]; 
        }
        printf("\nSum of Row %d: %d\n", i + 1, sum);
        printf("\n");
    }

    return 0;
}