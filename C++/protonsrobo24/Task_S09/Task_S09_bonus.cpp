#include <iostream>
using namespace std;
int main(){
    int count ;
    cout << "Please Enter how many time do u want to print:\n" << ">> ";
    cin >> count ;
    cout << "\tfor loop!\n";
    for (int i = 0; i < count; i++)
    {
        cout << "i am happy\n" ;
    }
    
    cout << "\twhile loop!\n";
    while (count != 0)
    {
        cout << "i am happy\n" ;
        count --;
    }
    

    return 0 ;
}