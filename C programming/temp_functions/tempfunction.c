#include<stdio.h>
#include<math.h>

void tempfunction(float temp);

int main()
{
    float temp;
    printf("Enter temperature in degree celsius:");
    scanf("%f",&temp);
    tempfunction(temp);
    return 0;
}

void tempfunction(float temp){
if(temp<0)
    printf("Freezing weather");
else if(temp>=0 && temp<10)
    printf("Very Cold Weather");
else if(temp>=10 && temp<20)
    printf("Cold Weather");
else if(temp>=20 && temp<30)
    printf("Normal in Temp");
else if(temp>=30 && temp<40)
    printf("Its Hot");
else
    printf("Its Very Hot");
}
