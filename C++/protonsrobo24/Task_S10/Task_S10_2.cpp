#include <iostream>
using namespace std;

void inarray(int arr[], int n)
{
    cout << "Please Enter " << n << " integers: \n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

void ReversiedArr(int arr[], int n)
{
    cout << "Reversed array: ";
    for (int i = (n-1); i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
}

int main()
{

    int n;

    cout << "\nEnter the number of elements in the array:\n" << ">> ";
    cin >> n;

    int arr[n];

    inarray(arr, n);

    ReversiedArr(arr, n);

    return 0;
}