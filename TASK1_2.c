#include <stdio.h>
#include <stdlib.h>

main()
{
    int num;
    printf("enter the countdown period: ");
    scanf("%d", &num);


    while (num >= 1)
    {
         printf("%d\n", num);
         num --;
    }
    printf("Blast off the moon!");

}
