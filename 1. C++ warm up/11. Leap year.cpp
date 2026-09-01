#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        bool leapyear(int y){
            if(y%4 == 0){
                if(y%100 == 0){
                    if(y%400 == 0){
                        return true;
                    }else{
                        return false;
                    }
                }else{
                    return true;
                }
            }else{
                return false;
            }
        }
};

int main(){
    int y = 2024;
    // cout<<"Enter the year: ";
    // cin>>y;
    Solution s;
    if(s.leapyear(y))
        cout<<y<<" is leap year";
    else
        cout<<y<<" isn't leap year.";
    return 0;
}