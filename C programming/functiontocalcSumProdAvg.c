#include <stdio.h>
void dowork(int a, int b, int *sum, int *product, int *average);
int main()
{
    int a, b;
    int sum, product, average;
    printf("enter the value of a :");
    scanf("%d", &a);
    printf("Enter the value of b :");
    scanf("%d", &b);
    dowork(a, b, &sum, &product, &average);
    printf("sum is %d product is %d average is %d",sum , product, average);
    return 0;
}
void dowork(int a, int b, int *sum, int *product, int *average)
{
    *sum = a + b;
    *product = a * b;
    *average = (a + b) / 2;
}