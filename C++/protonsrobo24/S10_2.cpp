#include <iostream>

using namespace std;

void maxmin(int arr[],int size ){
    
    int max ;
    int mainmun ;
    for (int i = 0; i <= size;i++)
    {
        
        if (arr[i] > max)
        {
            max = arr[i] ;
        }
        if (arr[i] < mainmun)   
        {
            mainmun = arr[i];
        }
        
    }
    cout << max << mainmun << "\n";
}
int main (){
    int arr[] = {1,2,3,4,5,6};
    int sz ; 
    sz  =sizeof(arr)/sizeof(int);
    maxmin (arr,sz);

    return 0 ;
}
