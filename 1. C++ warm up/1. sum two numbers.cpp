#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int add(int a, int b){
        return a+b;
    }
};

int main(){
    int a, b;
    cout<<"Enter two number: "<<endl;
    cin>>a>>b;
    Solution ob;
    cout<<ob.add(a,b);
    return 0;
}