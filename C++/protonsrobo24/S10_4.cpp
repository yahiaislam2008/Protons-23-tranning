#include <iostream> 
using namespace std;
int factorile(int num){
    int result =1 ;
    for (int i = 1; i <= num; i++)
    {
        result *= i ;
    }
    return result ;   
}


int main ()
{
    int num ;
    cout << "enter a number: " ;
    cin >> num ;
    cout << factorile(num);

    return 0;
}