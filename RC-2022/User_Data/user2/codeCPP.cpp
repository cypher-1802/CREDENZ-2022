#include "/home/rc/RC-2022/sandbox/filter/filter.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <string>
#define ll long long

using namespace std;

int main(){
put_filter();

    int n, m, a, b;  
     
    cin>>n>>m>>a>>b;  
    
    if(m * a <= b){
        cout<<n*a<<"\n";
    }else{
        cout<<(n/m)*b + min(n %m * a , b)<<endl;
    }

}