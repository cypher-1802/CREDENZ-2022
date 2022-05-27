#include "/home/rc/RC-2022/sandbox/filter/filter.h"
#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
put_filter();

    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n;
        cin>>n;
        switch(n%10)
        {
            case 1:cout<<67<<endl;
            break;
            case 2:cout<<82<<endl;
            break;
            case 3:cout<<69<<endl;
            break;
            case 4:cout<<68<<endl;
            break;
            case 5:cout<<69<<endl;
            break;
            case 6:cout<<78<<endl;
            break;
            case 7:cout<<90<<endl;
            break;
            case 8:cout<<50<<endl;
            break;
            case 9:cout<<46<<endl;
            break;
            case 0:cout<<67<<endl;1
            break;
        }
    }
    return 0;
}