#include <iostream>

int main(){
    using std::cout ;
    using std::cin;
    // std::string name ;
    // int science ;
    // int math ;
    // std::cout << "what is your name: \n";
    // std::cin >> name ;
    // std::cout << "what is the mark of science: \n";
    // std::cin >> science ;
    // std::cout <<"what is thr mark of math: \n";
    // std::cin >>math ;
    // std::cout <<(science+math)/2<<std::endl;
    // std::cout << name.size();
    
    // for (int i = 1; i < 6; i++)
    // {   
    //     std::string star (i, '*');
    //     std::cout << star << '\n';
    // }

    double age ;
    int age1St = 15 ;
    int age2nd = 9 ; 
    int agelater = 5 ;
    double finalage;
    cout << "please enter your age: \n" << ">> ";
    cin >> age ;
    finalage = (age / age1St) +((age-15)/age2nd) + ((age-24)/agelater);
    cout << "your age if u were a dog is : " << finalage << "\n";
    

    return 0 ;
}