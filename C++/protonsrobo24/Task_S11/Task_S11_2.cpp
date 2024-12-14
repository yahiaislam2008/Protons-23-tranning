#include <iostream>
using namespace std;

void inarray(int arr[] , int n)
{
    
    cout << "Please Enter " << n << " integers: \n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

bool Duplicate(int arr[] , int n)
{
    for (int i = 0; i < n-1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] == arr[j])
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int nums[4];
    int n ;
    cout << "Enter the number of elementes u want: \n" << ">> ";
    cin >> n ;
    inarray(nums , n);
    
    if (Duplicate(nums , n) == true)
    {
        cout << "true";
    }
    else
    {
        cout << "false";
    }

    return 0;
}