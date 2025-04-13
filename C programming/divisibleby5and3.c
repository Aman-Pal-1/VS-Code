#include <stdio.h>

int main (){
    int val1, val;
    printf("Enter the Value :");
    scanf("%d",&val1);
    if (val1%3==0 && val1%5==0){
        printf("%d is completely divisible by both 3 and 5 .",val1);
    }
    else if (val1%3==0){
        printf("%d is completely divisible by 3 . ",val1);
    }
    else if (val1%5==0){
        printf("%d is completely divisible by 5 . ",val1);
    }
    return 0;
}