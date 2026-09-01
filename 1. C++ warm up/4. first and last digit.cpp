#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        pair<int, int> findDigit(int num){
            int first_digit = num/1000;
            int last_digit = num%10;
            return {first_digit, last_digit};
        }
};

int main(){
    int num;
    cout<<"Enter 4 digit number: ";
    cin>>num;
    Solution ob;
    pair<int, int> p = ob.findDigit(num);
    int a = p.first;
    int b = p.second;
    cout<<"First digit "<<a <<" Last digit " <<b;
    return 0;
}