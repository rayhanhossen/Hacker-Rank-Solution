#include<stdio.h>


int main(){
    int a, b, Isum, Idiff;
    float c, d, Fsum, Fdiff;

    scanf("%d %d", &a, &b);
    scanf("%f %f", &c, &d);

    //sum of two integer number
    Isum = a + b;
    // difference of two intiger number
    Idiff = a - b;

    // sum of two float number
    Fsum = c + d;
    // difference of two float number 
    Fdiff = c - d;

    printf("%d %d\n",Isum, Idiff);
    printf("%.1f %.1f\n",Fsum, Fdiff);

    return 0;


}