#include <stdio.h>
#include <stdlib.h>


float mpu6050[10] = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26};
float bno55[10] = {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69};
float average_array[10];
float ac1 = .79;
float ac2 = .92;
int main()
{
    int j;
    int i;
    float average_element;
    for (i = 0; i<10; i++)
    {
        /*calculating an output using the accuracy of each output*/
        average_array[i] = ((mpu6050[i]/ac1 * ac1) + (bno55[i]/ac2 *ac2)) / ((1 / ac1 * ac1) + (1 / ac2 * ac2));

    }
    printf("the result of the sensor fusion:\n\n");
    /*printing the resulting array*/
    printf("{ ");
    for (j = 0; j < 10; j++)
        printf("%f  ", average_array[j]);
    printf(" }");


}