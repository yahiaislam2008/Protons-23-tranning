#include <iostream>
#include <cmath>

int main(){
    using std::cout ;
    using std::cin;
    
    double num1 ;
    double num2 ;
    int result ;
     
    cout << "Please Enter a first number (bigger number first): \n" << ">> ";
    cin >> num1 ;

    cout << "Please Enter a second num : \n" << ">> ";
    cin >> num2 ;
    
    cout << "Addition: " << (num1 + num2) << "\n" ;

    cout << "Subtraction: " << (num1 - num2) << "\n" ;

    cout << "Multiplication: " << (num1 * num2) << "\n" ;

    cout << "Float Division: " << (num1 / num2) << "\n" ;

    result = (num1 / num2) ;
    cout << "Integer Division: " << result << "\n" ;

    cout << "Power: " << pow(num1,num2) << "\n" ;


    cout << "Square root: " << sqrt(num2) << "\n" ;

    return 0 ;
}