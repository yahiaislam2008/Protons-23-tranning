#include <iostream>
#include <ctime>

using std::cout;
using std::cin;


char getuser(){
    char player ;
    
    do
    {
    cout << "chosse one (rock(r) paper(p) scissors(s))\n" << "(r-p-s) >> ";
    cin >> player;
    cout << "\n" <<"\n" <<"\n" <<"\n"<<"\n"<<"\n";
    } while (player != 'r'&& player != 's' && player != 'p');
    
    return player ; 
}
void showchoice(char choice){
    if (choice == 'r')
    {
        cout << "Rock\n" ;
    }
    else if (choice == 's')
    {
        cout << "scissors\n" ;
    }
    else if (choice == 'p')
    {
        cout << "paper\n" ;
    }
    else 
    {
        cout << "invalide\n" ;
    }
}
char getcomputer(){
    srand(time(0));
    int num = rand() % 3 + 1 ;
    if (num == 1)
    {
        return 'r';
    }
    else if (num == 2)
    {
        return 's';
    }
    else
    {
        return 'p';
    }
    
}
void showwinner (char player1 , char player2){
    if (player1 == player2)
    {
        cout << "it's a tie!\n"; 
    }
    else if ((player1 == 'r' && player2 == 's') || (player1 == 's' && player2 == 'p') || (player1 == 'p' && player2 == 'r'))
    {
        cout << "player1 won\n";
    }
    else 
    {
        cout << "player1 lose\n";
    }
    
    
}

int main(){
    char continuer ;
    int choice;
    cout << "**** Welcome to our game ****\n" << "**** rock paper scissors ****\n";


    do
    {
        cout << "choise:\n" << "1.play VS computer\n" << "2.play VS friend\n";
        cin >> choice;
        if (choice ==1)
        {
            char player = getuser();
            char computer = getcomputer();
            cout << "your choice is: " ;
            showchoice(player);
            cout << "computer choice is: " ;
            showchoice(computer);
            showwinner(player,computer);
        }else
        {
            char player1 = getuser();
            char player2 = getuser();
            cout << "your choice is: " ;
            showchoice(player1);
            cout << "friend choice is: " ;
            showchoice(player2);
            showwinner(player1,player2);
        }
 
        do
        {
            cout << "do u want to play again\n"<<"(y/n) >> ";
            cin >> continuer ;            
        } while (continuer != 'y' && continuer != 'n');
        if (continuer == 'y')
        {
            continue;
        }
        else
        {
            break;
        }
        
        
    } while (true);
    
    
    return 0;
}