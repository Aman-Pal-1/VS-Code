#include <stdio.h>
#define N 5
int main()
{
    int a[N], i, *ptr;
    printf("Enter the array %d elements :", N);
    for (i = 0; i <= N-1; i++)
    {
        scanf("%d", &a[i]);
    }
    ptr = &a[N - 1];
    for (i = 0; i <= N-1; i++)
    {
        printf("%d ", *ptr--);
    }
    return 0;
}