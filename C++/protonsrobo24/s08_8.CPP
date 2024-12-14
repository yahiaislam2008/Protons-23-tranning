#include <iostream>

int main()
{

    int x;
    int y;
    char opporation;

    std::cin >> x >> opporation >> y;

    switch (opporation)
    {
    case '+':
        std::cout << x + y;
        break;
    case '-':
        std::cout << x - y;
        break;
    case '/':
        std::cout << x / y;
        break;
    case '*':
        std::cout << x * y;
        break;
    default:
        std::cout << "wrong opporation";
        break;
    }
}