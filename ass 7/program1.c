// C program to demonstrate 
// Flawfinder
#include <stdio.h>
#include <string.h>
  
// Driver code
int main()
{
    char temp[];
    char str[] = "hello\0";
    strcpy_s(temp, str);
    printf("%s", temp);
    return 0;
}