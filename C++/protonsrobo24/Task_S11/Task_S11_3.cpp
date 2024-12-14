#include <iostream>
using namespace std;

float Power(float num , float n){
    float result = 1;
    if (n == 0)
    {
        result = 1;
    }else if (n == 1)
    {
        result = num ;
    }
    else if (n < 0)
    {
        n *= -1 ;
        for (int i = 1; i <= n; i++)
        {
            result *= num;
        }
        result = 1/result ;
    }
    else
    {
        for (int i = 1; i <= n ; i++)
        {
            result *= num ;
        }
        
    }
    return result ; 
    
    
}


int main(){

    float num ;
    float PoNum ;
    
    cout << "\n****** Power programe ******\n"; 

    cout << "Enter Your Number: \n" << ">> " ;
    cin >> num ;

    cout << "Enter the Power number: \n" << ">> ";
    cin >> PoNum ;

    cout << Power(num , PoNum) << "\n" ;

    return 0 ;
}