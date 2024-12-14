#include <iostream>
using namespace std;
int main(){

    char grade ;

    cout << "Enter you grade (A, B, C, D, F):\n" << ">> ";
    cin >> grade ;

    switch (grade)
    {
    case 'A':
        cout << "Excellent!\n";
        break;
    case 'B':
        cout << "Good job!\n";
        break;
    case 'C':
        cout << "Well done!\n";
        break;
    case 'D':
        cout << "You passed!\n";
        break;
    case 'F':
        cout << "Better luck next time!\n";
        break;
    default:
        cout << "Invalid grade! Please enter A, B, C, D, or F\n" ;
        break;
    }

    return 0 ;
}