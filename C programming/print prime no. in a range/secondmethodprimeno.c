#include<stdio.h>

int main(){
    int a,b,i,j;
    printf("Enter the Value of a , b :");
    scanf("%d %d", &a, &b);
    for(i=a;i<=b; i++){
        for(j=2; j<=i; j++){
            if(i%j==0)
            break;
        }
    if (i==j)
    printf("%d\n",j);
    }
    return 0;

}