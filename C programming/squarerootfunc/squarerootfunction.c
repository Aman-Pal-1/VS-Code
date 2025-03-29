#include <stdio.h>
#include <math.h>
void square_root(double n);
int main ()
{
    double n;
    printf("Enter the number: ");
    scanf("%lf",&n);
     square_root(n);
    return 0;
}

void square_root(double n){
    if (n < 0){
        printf("the no is negative so root is not real.\n");
    }else {
        double result =sqrt(n);
        printf("The Square Root is : %.2f\n", result);
    }
}