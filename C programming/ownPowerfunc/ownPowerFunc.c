#include <stdio.h>

double mypow(double base, int exponent);

int main()
{
    double base;
    int exponent;

    printf("Enter the base value: ");
    scanf("%lf", &base);
    printf("Enter the exponent: ");
    scanf("%d", &exponent);

    double result = mypow(base, exponent);
    printf("%.2lf raised to the power of %d is %.2lf\n", base, exponent, result);

    return 0;
}

double mypow(double base, int exponent)
{
    double result = 1.0;
    int absExponent = (exponent < 0) ? -exponent : exponent; // Handle negative exponents

    for (int i = 0; i < absExponent; i++) {
        result *= base; // Multiply base absExponent times
    }

    if (exponent < 0) {
        result = 1.0 / result; // Take reciprocal for negative exponents
    }

    return result;
}