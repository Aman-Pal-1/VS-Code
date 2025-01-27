#include <stdio.h>

int main(){
    int a;
    printf("Enter the value of a :");
    scanf("%d",&a);
    if (a%3==0){
        if (a%5==0){
            printf("%d is divisible by 3 & 5 .",a);
        }
        else if (a%5!=0){
            printf("%d is divisible by 3 not divisible by 5 .",a);
        }
    }
    if (a%3!=0){ 
        if (a%5==0){
            printf("%d is not divisible by 3 but divisible by 5 .",a);
        }
    }
    if(a%3!=0){
        if (a%5!=0){
        printf(
         "%d is not divisible by both 3 and 5 .",a
        );
        }
    }
    return 0;
}