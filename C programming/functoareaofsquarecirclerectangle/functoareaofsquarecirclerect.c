#include<stdio.h>
#include<math.h>

float area_of_circle(float r);
float area_of_rectangle(float l, float b);
float area_of_square(float s);

int main ()
{
    float r,l,b,s;
    printf("Enter the radius of the circle:");
    scanf("%f",&r);
    printf("area of circle is %f :\n ",area_of_circle(r));

    printf("Enter the length and breadth of the rectangle:");
    scanf("%f %f",&l,&b);
    printf("area of rectangle is %f :\n" , area_of_rectangle(l,b));

    printf("Enter the side of the square :");
    scanf("%f",&s);
    printf("area of square is %f", area_of_square(s));
    
    return 0;
}


float area_of_circle(float r)
{
    float area=3.14*r*r;
    return area;
}

float area_of_rectangle(float l,float b){
    float area = l*b;
    return area;
}

float area_of_square(float s){
    float area= s*s;
    return area;
}