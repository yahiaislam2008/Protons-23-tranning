#include <iostream>
#include <cmath>
using namespace std;
bool prime(int num ){
     
    int c =0 ;
    for(int i=2; i<=num; i++){
        if (num % i == 0 )
        {
            c++;
        }
    }
    if (c==1)
        {
            return true ;
        }
        else
        {
            return false;
        }  
}
int main(){
    int num ;

    cout << "enter a number: " ;
    cin >> num ;
    bool isprime = prime(num);
    if (isprime == true )
    {
        cout << "the number is prime";
    }
    else
    {
        cout << "the number is not prime";
    }
    
    
    return 0;
}