#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        bool magicNumber(int n){
            int temp = n;
            int last_digit = temp%10;
            int first_digit;
            while(temp >= 10){
                temp/= 10;
            }
            first_digit = temp;

            if(first_digit + last_digit == 10) return true;
            else return false;
        }
};

int main(){
    int n;
    cout<<"Enter the numbers: ";
    cin>>n;
    Solution s;
    cout<<boolalpha<< s.magicNumber(n);
    return 0;
}