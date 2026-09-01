#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        pair<int, int> swap(int a, int b){
            int temp = a;
            a = b;
            b = temp;
            return {a, b};
        }

        pair<int, int> _swap(int a, int b){
            b = a + b - (a = b);
            return {a, b};
        }
};

int main(){
    int a, b;
    cout<<"Enter two numbers: ";
    cin>>a>>b;
    cout<<"Before swapping:\na = "<<a<<" b = "<<b<<endl;
    
    Solution obj;
    pair<int, int> p = obj._swap(a, b);
    cout<<"After swapping:\na = "<<p.first<<" b = "<<p.second<<endl;
    return 0;
}