#include<stdio.h>

int main (){
    int n;
    printf("Enter a number : ");
    scanf("%d",&n);
    for(int i=1;i<n;i++){
        for(int j=1;j<=n;j++){
     int a= n/2+1;
            if(i==3|| j==3){
                printf("*");
            }
            else{ printf(" ");
            }
        }

    }
    return 0;
}