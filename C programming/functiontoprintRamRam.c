#include<stdio.h>

void ramram();
void bonjour();

int main()
{
    printf("enter the f for french and i for indian \n");
    char ch;
    scanf("%c",&ch);
    if (ch=='f'){
        bonjour();
    }
    else if (ch=='i'){
        ramram();
    }
    else{
        printf("invalid input \n");
    }
    return 0;

}


void ramram(){
    printf("ram ram \n");
}


void bonjour(){
    printf("bonjour \n");
}