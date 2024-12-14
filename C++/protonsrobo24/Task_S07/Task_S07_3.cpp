#include <iostream>

int main(){
    using std::cout ;
    using std::cin;
    
    std::string name ;
    double age ;
    double height;

    cout << "Please Enter your name: \n" << ">> ";
    cin  >> name ;

    cout << "Please Enter your age: \n" << ">> ";
    cin  >> age ;

    cout << "Please Enter your height: \n" << ">> ";
    cin  >> height ;

    cout << "Hello " << name << ", you are " << age << " years old and your height is " << height << "\n";
    

    return 0 ;
}