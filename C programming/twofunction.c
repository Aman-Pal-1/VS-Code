#include <stdio.h>
void namaste();
void bonjour();

int main (){
    printf("enter f for french & i for indian: \n ::");
    char ch;
    scanf("%c", &ch);
    if(ch=='f'){
        printf("You are french\n");
        bonjour();
    }
    else if(ch=='i'){
        printf("You are indian\n");
        namaste();
    }
    else{
        printf("invalid\n");
    }
    return 0;
}

 void namaste(){
    printf("namaste\n");
 }
 void bonjour(){
    printf("bonjour\n");
 }