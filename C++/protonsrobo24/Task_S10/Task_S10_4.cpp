#include <iostream>

using namespace std;

int Factorial(int num){
    int result =1;

    for (int i = 1; i <= num; i++)
    {
        result *= i ; 
    }
    return result ;   
}

int main(){

    int num ;

    cout << "\nPlease Enter a great number:\n" << ">> ";
    cin >> num ;

    int result = Factorial(num);

    cout << "\nThe factorial of " << num << " is " << result << endl;


    return 0 ;
}