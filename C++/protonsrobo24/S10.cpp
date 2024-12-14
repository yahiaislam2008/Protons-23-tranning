#include <iostream>
using namespace std;
int count(int num1, int num2)
{
    int sum = 0;
    for (int i = num1; i <= num2; i++)
    {
        if (i % 9 == 0)

        {
            sum += i;
        }
    }
    return sum;
}

int main()
{
    int a, b;
    cout<<"enter 2 numbers\n";
    cin>>a >> b;
    cout << count(a, b);
}