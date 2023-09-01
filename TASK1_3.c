#include <stdio.h>
#define MAX 20
char task_array[20][100];
int ID_array[20];
int position = 0;


void add_func()
{

    char buff[100]; // Add a buffer to clear the input buffer
    fgets(buff, 100, stdin); // Add a buffer to clear the input buffer
    printf("enter task description :\n");
    fgets(task_array[position], 100, stdin);
    ID_array[position] = position + 1;
    printf("task added successfully! ");
    position++;



}


void view_func()
{
    int i;
    for (i = 0; i < position; i++)
    {
        printf("task %d %s\n", i + 1, task_array[i]);
        printf("ID: %d\n", i + 1);


    }

}




void remove_func()
{
    int index;
    int i;
    printf("enter the task ID to remove: ");
    scanf("%d", &index);

    if (index >= 1 && index <= position) {
        for (i = index - 1; i < position - 1; i++) {
            strcpy(task_array[i], task_array[i + 1]);
            ID_array[i] = ID_array[i + 1];
        }
        position--;
    } else {
        printf("Invalid task ID!\n");
    }
    int z;
    printf("the new task list:\n");
    for (z = 0; z < position; z++)
    {
        printf("\n");
        printf("task %d %s\n", z + 1, task_array[z]);
        printf("ID: %d\n", z + 1);


    }

}


void main()
{


    int keep = 1;
    while (keep == 1)
    {
        int action;
        printf("missions task manager.\n");
        printf(" 1.Add task\n 2.View tasks\n 3.Remove tasks\n 4.exit\n choose the action number: ");
        scanf("%d", &action);

        switch (action)
        {
            case 1:
                add_func();
                break;
            case 2:
                view_func();
                break;
            case 3:
                remove_func();
                break;
            case 4:
                break;
        printf("do you want to commit another action '1' for yes  '0' for no: ");
        scanf("%d", &keep);
        if (keep == 0)
        {
            printf("end program.");
        }



        }





    }



}



