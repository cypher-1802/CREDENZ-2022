#include "/home/rc/RC-2022/sandbox/filter/filter.h"
#include<bits/stdc++.h>
using namespace std;

int main()
{
put_filter();

    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int a=n%10;
        if(a==1)
        {
            cout<<67<<endl;
        }
        else if(a==2)
        {
             cout<<82<<endl;
        }
         else if(a==3)
        {
             cout<<69<<endl;
        }
         else if(a==4)
        {
             cout<<68<<endl;
        }
         else if(a==5)
        {
             cout<<69<<endl;
        }
         else if(a==6)
        {
             cout<<78<<endl;
        }
         else if(a==7)
        {
             cout<<90<<endl;
        }
         else if(a==8)
        {
             cout<<50<<endl;
        }
         else if(a==9)
        {
             cout<<46<<endl;
        }
        else
        {
            cout<<48<<endl;
        }
    }
}