#include <stdio.h>

int main()
{
    double x1, x2, x3, y1, y2, y3, slope;
    printf("Remember: the type of value you are solving for needs to be Y values");
    printf("\nEnter y2, y1, x2, x1 in that order: \n");
    scanf("%lf \n%lf \n%lf \n%lf", &y2, &y1, &x2, &x1);
    slope = (y2-y1)/(x2-x1);
    //printf("%lf", slope);
    printf("Enter the third X value that you know: \n");
    scanf("%lf", &x3);
    y3 = (slope * (x3-x1)) + y1;
    printf("Unknown value is: \n%lf", y3);
    
    
    
    return 0;
}

