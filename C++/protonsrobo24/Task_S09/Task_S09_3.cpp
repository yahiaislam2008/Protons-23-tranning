#include <iostream>
using namespace std;
int main(){
    double totalpurchase;
    int membership;
    int complaints ;
    int purchases ;
    double discount ;

// Collect Customer Information
    cout << "Enter the total purchase amount: ";
    cin >> totalpurchase ;

    cout <<"Enter the number of membership: ";
    cin >> membership ;

    cout << "Enter the number of complaints filed in the past year: ";
    cin >> complaints ;

    cout << "Enter the number of purchases made in the past year: " ;
    cin >> purchases ;

//adjust discount for membership
    if (membership > 10)
    {
        discount = 10 ;
    }
    else if (membership <= 10 && membership >=6)
    {
        discount = 8 ;
    }
    else
    {
        discount = 5;
    }

//adjust discount for complaints
    complaints *= 2;
    discount -= complaints;
    
    if (discount < 0)
    {
        discount =0 ;
    }
    
// Apply Bonus Reward for Frequent Purchases

    if (purchases >= 20)
    {
        discount = 5 ;
    }
    
// calculation
    discount /= 100 ;
    discount *= totalpurchase;

    totalpurchase -= discount ;

    cout << "Net discount amount: " << discount << "\n";
    cout << "Net total purchase amount: " << totalpurchase << "\n";


    return 0 ;
}