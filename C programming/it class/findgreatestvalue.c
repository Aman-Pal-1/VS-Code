#include<stdio.h>
int main(){
    int a,b,c;
    printf("GIVE THREE INTEGER VALUES\n");
    printf("Enter the value of a : ");
    scanf("%d",&a);
    printf("Enter the value of b : ");
    scanf("%d",&b);
    printf("Enter the value of c : ");
    scanf("%d",&c);
    if (a>b && a>c){
        printf("The value of a is %d is the greatest value .",a);
    }
    if(b>a && b>c){
        printf("The value of b is %d is the greatest value .",b);
    }
    if (a == b == c){
        printf("All values are Equal");
    }
    if (a == b){
        printf("Value of a and b are Equal. ");
    }
    if (c == b){
        printf("Value of c and b are Equal. ");
    }
    if (a == c){
        printf("Value of a and c are Equal. ");
    }
    if (c>a && c>b){
        printf("The value of c is %d is the greatest value .",c);
    }
   return 0;
}