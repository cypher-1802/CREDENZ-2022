#include "/home/rc/RC-2022/sandbox/filter/filter.h"
#include <stdio.h>
#include <string.h>

int main(void)
{
put_filter();

    int t = 0;
    scanf("%d", &t);
    
    int n[t];
    for( int i = 0; i < t; i++)
    {
        scanf("%d", &n[i]);
    }
    int ar[10] = {48, 67, 82, 69, 68, 69, 78, 90, 50, 46};
    
    for(int i = 0; i < t; i++)
    {
        while (n[i] >= 10)
        {
            n[i] = n[i]%10;
        }
        printf("%d\n", ar[n[i]]);
    }
    return 0;
}