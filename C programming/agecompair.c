#include <stdio.h>

int main (){
    int rm, sm, ay;
    printf("Enter the age of ram : ");
    scanf("%d",&rm);
    printf("Enter the age of shyam : ");
    scanf("%d",&sm);
    printf("Enter the age of ajay : ");
    scanf("%d",&ay);
    if(rm>sm && rm>ay){
        printf("Ram is Younger then other");
    }
    if(sm>rm && sm>rm){
        printf("Shyam is Younger then other");
    }
    if (sm==rm==ay){
        printf("All have same age.");
    }
    if (sm==rm==ay<0){
        printf("age is not negative");
    }
    else if (ay>rm && ay>sm){
        printf("Ajay is Younger then other");
    }
    return 0;
}