#include <iostream>

int main(){
    using std::cout ;
    using std::cin ;

    int num ;
    int digit ;
    cout << "Please Enter 4 digit: \n" << ">> "; 
    cin >> num;
    
    digit =num % 10 ;
    cout << digit << "\n";

    num /= 10;

    digit =num % 10 ;
    cout << digit << "\n";

    num /= 10;

    digit =num % 10 ;
    cout << digit << "\n";

    num /= 10;

    digit =num % 10 ;
    cout << digit << "\n";


    return 0 ;
}