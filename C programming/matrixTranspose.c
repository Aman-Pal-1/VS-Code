#include <stdio.h>

int main()
{
    int r, c;
    printf("Enter the no. of rows:");
    scanf("%d", &r);
    printf("Enter the no. of columns:");
    scanf("%d", &c);
    int arr[r][c];
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("Enter Value :");
            scanf("%d", &arr[i][j]);
        }
    }
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%d ", arr[i][j]);
        }
            printf("\n");
    }
    for (int i = 0; i < c; i++)
    {
        printf("\n");
        for (int j = 0; j < r; j++)
        {
            printf("%d ", arr[j][i]);
        }
    }

    return 0;
}