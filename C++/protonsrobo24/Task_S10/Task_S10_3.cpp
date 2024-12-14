#include <iostream>
#include <cmath>

using namespace std;

bool CheckPrime(int num)
{
    int temp = 0 ;
    if (num == 0 || num == 1)
    {
        return false ;
    }

    else
    {
        for (int i = 2; i < num; i++)
        {
            if (num % i == 0 )
            {
                temp ++ ;
            }
        }
        if (temp == 0)
        {
            return true ;
        }
        else
        {
            return false ;
        }       
    }
}

int main()
{
    int num;

    cout << "\nPlease Enter a number: \n" << ">> ";
    cin >> num;

    bool isprime = CheckPrime(num);

    if (isprime == true)
    {
        cout << num << " is a prime number!\n";
    }
    else
    {
        cout << num << " is not a prime number!\n";
    }
    
    return 0;
}