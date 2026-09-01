#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        bool Palindrome(int n){
            int temp = n;
            int reverse = 0;

            while(temp > 0){
                int digit = temp%10;
                reverse = reverse*10 + digit;
                temp/= 10;
            }
            if(reverse == n)
                return true;
            else
                return false;
        }

        bool isPrime(int n){
            if(n <= 1)  return false;

            for(int i = 2; i <= sqrt(n); i++){
                if(n%i == 0)
                    return false;
            }
            return true;
        }
};

int main(){
    int n = 131;
    // cout<<"Enter the numbers: ";
    // cin>>n;
    Solution s;
    if(s.Palindrome(n) == 1 && s.isPrime(n) == 1)
        cout<<n<<" is PalPrime Number.";
    else
        cout<<n<<" isn't PalPrime.";
    return 0;
}