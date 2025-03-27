#include<stdio.h>
#include<math.h>

void sumofDigits(int n, int sum);
int main()
{
    int n, r,sum=0;
    printf("Enter a number: ");
    scanf("%d",&n);
    
    while (n>0) {
        r=n%10;
        sum=sum+r;
        n=n/10;
    }
    sumofDigits(n,sum);
    return 0;
}

void sumofDigits(int n, int sum)
{
    printf("Sum of digits is: %d",sum);
}