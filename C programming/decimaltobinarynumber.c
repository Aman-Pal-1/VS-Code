#include<stdio.h>
int main(){
    int i=0,j,n=20,a;
    for(i=0; n>0; i++)
    {
        a=n%2;
        n=n/2;
        i++;
        printf("%d/n",a);

    }
    for(i=i-1;i>=0;i--)
    {
        printf("%d",i);
    }
    return 0;
}