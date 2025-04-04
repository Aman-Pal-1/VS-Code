//wap in c to find the maximum number b/w two no.s using a pointer?
#include <stdio.h>

int main (){
    int a,b;
    printf("Enter the value of a and b :");
    scanf("%d %d",&a, &b);
    int *l = &a;
    int *m = &b;
    if (*l>*m){
        printf("the greater value is %d", a);
    }
    if(*l<*m){
        printf("the greater value is %d", b);
    }
    return 0;
}