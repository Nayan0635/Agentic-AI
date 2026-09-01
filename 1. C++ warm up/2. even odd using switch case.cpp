#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    void checkNum(int num){
        switch(num%2){
            case 0:
                cout<<num<<" is even number";
                break;
            case 1:
            case -1:
                cout<<num<<" is odd Number.";
                break;
            default:
                cout<<"Invalid input";
        }
    }
};

int main(){
    int num;
    cout<<"Enter the number: ";
    cin>>num;
    Solution ob;
    ob.checkNum(num);
    return 0;
}