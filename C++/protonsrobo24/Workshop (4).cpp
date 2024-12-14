#include <iostream>
using namespace std;
int main()
{

    int salary;
    int years;
    double bonus =10 ;
    cin >> salary;
    cin >> years;

    if (years >= 10)
    {
        salary +=((bonus /100) * salary);
        cout << salary;
    }
    else if ((years < 10) && (years >= 6))
    {
        bonus = 8;
        salary += ((bonus / 100) * salary);
        cout << salary;
    }
    else
    {
        bonus = 5;
        salary += ((bonus / 100) * salary);
        cout << salary;
    }
    
}