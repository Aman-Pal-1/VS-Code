#include<stdio.h>
int main()
{
    num[4]=[1,2,3,4];
   int num[0];
   for(int i=1;i<=4;i++)
   {
     num[i]=num[i]+num[i-1];
   }
   return 0;
}