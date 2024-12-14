#include <iostream>

using namespace std;

int main()
{

    int selection;
    int quantity;
    double paid;
    double Changedue =0;
    double totalcost =0;
    cout << "\n******** Welcome to the Vending Machine! ********\n";

    cout << "1. Soda ($1.00)\n2. Chips ($0.75)\n3. Candy ($0.50)\n";
    cout << "Enter your selection (1-3): \n" << ">> ";
    cin >> selection;

    cout << "Enter the quantity you want:\n" << ">> ";
    cin >> quantity;

    cout << "Please enter the amount you paid:\n" << ">> $";
    cin >> paid;
    
    if (selection == 1)
    {
        totalcost = quantity * 1;
    }
    else if (selection == 2)
    {
        totalcost = quantity * 0.75;
    }
    else if (selection == 1)
    {
        totalcost = quantity * 0.75;
    }
    else
    {
        cout << "invaild input\n";
    }

    if (paid > 5.00)
    {
        cout << "Congratulations! You've spent over $5.00. You received a 10% discount. \n";
        totalcost= paid - (0.1 * paid);
        Changedue = (0.1 * paid);
    }
    
    cout << "Total cost:$ " << totalcost << "\n";
    cout << "Change due:$ " << Changedue << "\n";

    cout << "*************************************************\n";

    
}