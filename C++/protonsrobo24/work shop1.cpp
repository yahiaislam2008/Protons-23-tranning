#include <iostream>
using namespace std;
int main()
{
    int grade;
    cin >> grade;
    if (grade >= 60)
    {
        cout << "success";
    }
    else if (grade >= 50)
    {
        cout << "pass";
    }
    else
    {
        std::cout << "sa2at";
    }
}