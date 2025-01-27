#include<stdio.h>
void main(){
    int a[10],i;
    for(i=0;i<5;i++){
        printf("Enter the Number");
        scanf("%d",&a[i]);
        printf("output= %d\n", a[i]);
    }
}