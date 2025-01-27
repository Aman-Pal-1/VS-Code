#include<stdio.h>
int main (){
    int a,b;
    printf("Enter the buying prize: ");
    scanf("%d", &a);
    printf("Enter the Selling prize: ");
    scanf("%d", &b);
    if(a<0){
        printf("prices are not negative. please give correct value.");
    }
    else if (a>b){
        printf("your lose is : %d \n",a-b);
    }else if (a==b){
        printf("your buying price %d and your selling price %d so you have no profit and no loss. ",a ,b);
    }else{
        printf("your profit is : %d \n",b-a);
    }
    return 0 ;
}