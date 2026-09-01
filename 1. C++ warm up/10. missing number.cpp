#include<bits/stdc++.h>
using namespace std;

int main(){
    int arr[10] = {1, 2, 3, 4, 6, 7, 8, 9, 10};
    int s = sizeof(arr)/ sizeof(arr[0]);
    int total = 55;
    int sum = 0;
    for(int i = 0; i< s; i++){
        sum+= arr[i];
    }
    cout<<"missing number is-> "<<total-sum;
    return 0;
}