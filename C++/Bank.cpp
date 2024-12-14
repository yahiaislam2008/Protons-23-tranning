#include <iostream>

double depost(){
    double money = 0 ;
    std::cout << "how much do u want to depost: ";
    std::cin>>money;
    if (money > 0)
    {
        return money;
    }
    else
    {
        std::cout<<"invalide number: "<<"\n";
        return 0;
    } 
}
double showbalance(double balance){
    std::cout << "your current balance is:"<<balance<<"\n";
    return balance;   
}
double withdraw(double balance){
    double money =0;
    std::cout << "how much do u want to withdraw: ";
    std::cin>>money;
    if (money > 0 && money < balance)
    {
        return money;
    }
    else
    {
        std::cout<<"invalide number: "<<"\n";
        return 0;
    } 
}
int main(){

    double balance = 0;
    int choise=0;
    while (true)
    {
        std::cout << "\nchosse which operation u want"<<"\n";
        std::cout << "1.show balance\n"<<"2.depost money\n"<<"3.withdraw\n"<<"4.exit\n";
        std::cout << ">>";
        std::cin >> choise;
        if (choise == 1){
            showbalance(balance);
        }else if (choise == 2)
        {
            balance += depost();
            showbalance(balance);
        }else if (choise == 3)
        {
            balance -= withdraw(balance);
            showbalance(balance);
        }else
        {
            break;
        }
      
    }
    



    return 0;
}