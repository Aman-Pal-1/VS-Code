#include<stdio.h>
#include<math.h> // Include math.h for square root function.

int main() {
    int a, b, i, j, isPrime;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    printf("Enter the value of b: ");
    scanf("%d", &b);
    printf("Prime numbers between %d and %d are:\n", a, b);

    for(i = a; i <= b; i++) {
        if(i < 2) // Skip numbers less than 2.
            continue;

        isPrime = 1; // Assume the number is prime.
        for(j = 2; j <= sqrt(i); j++) { // Check up to square root of `i`.
            if(i % j == 0) { // If divisible, it's not prime.
                isPrime = 0;
                break;
            }
        }
        if(isPrime) {
            printf("%d\n", i);
        }
    }
    return 0;
}