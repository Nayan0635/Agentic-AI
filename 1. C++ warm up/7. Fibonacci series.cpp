#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        int fibonacci(int n){
            if(n == 0) 
                return 0;
            else if(n == 1)
                return 1;

            return fibonacci(n-1) + fibonacci(n-2);
        }
};

int main(){
    // int a = 0, b = 1, c;
    int n = 10;

    Solution s;
    for (int i = 0; i < n; i++){
        cout<<s.fibonacci(i)<<" ";
    }
    // for (int i = 0; i < n; i++){
    //     cout<<a<<" ";
    //     c = a+b;
    //     a = b;
    //     b = c;        
    // }
    
    return 0;
}