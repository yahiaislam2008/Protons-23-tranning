#include <iostream>
//iterative 
// void walk(int steps){
//     for (int i = 0; i < steps; i++)
//     {
//         std::cout << "you take a step!\n";
//     }
// }

// recursion
void walk(int steps){
    if (steps > 0)
    {
        std::cout << "you take a step!\n";
        walk(steps-1);
    }   
}

int factorial(int number){
//iterative
    // int result =1 ;
    // for (int i = 1; i <= number; i++)
    // {
    //     result = result * i;
    // }
    // return result ; 
// recursion
    if (number > 1)
    {
        return number * (factorial(number-1));
    }
    else
    {
        return number  ; 
    }       
}
void star(int stars){
    std::string Star(stars,'*');
    if (stars > 1)
    {
        std::cout << Star << "\n";
        star(stars -1);
    }
    else
    {
        std::cout << '*';
    }
}
int main(){
    using std::cout;
    using std::cin;
    walk(29);
    std::cout << factorial(6) << "\n";
    int stars ;
    cout << "enter how many stars u want '*': " ;
    cin >> stars ;
    star(stars);

    return 0 ; 
}