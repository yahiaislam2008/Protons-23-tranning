#include <iostream>
using namespace std;

void inarray(int arr[],int n){
    cout << "Please Enter " << n << " integers: \n" ; 
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i] ;
    }
}

int Maxnum(int arr[],int n){
    int max = 0 ;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }  
    }
    return max ;
}
int main(){
    int n ;
    int maximum;

    cout << "\nEnter the number of elements in the array:\n" << ">> ";
    cin >> n;

    int arr[n]; 

    inarray(arr , n);

    maximum = Maxnum(arr , n );

    cout << "The maximum value in the array is: " <<  maximum;


    return 0 ;
}