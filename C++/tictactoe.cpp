#include <iostream>

void drawboard(char *spaces){
    std::cout << "\n";
    std::cout << "\t\t\t\t\t  "<<  spaces[0] << "  |  " << spaces[1] << "  |   " << spaces[2] << "  \n";
    std::cout << "\t\t\t\t\t"<< "_____|_____|_____\n";
    std::cout << "\t\t\t\t\t  "<<  spaces[3] << "  |  " << spaces[4] << "  |   " << spaces[5] << "  \n";
    std::cout << "\t\t\t\t\t"<< "_____|_____|_____\n";
    std::cout << "\t\t\t\t\t  "<<  spaces[6] << "  |  " << spaces[7] << "  |   " << spaces[8] << "  \n";
    std::cout << "\t\t\t\t\t"<< "     |     |   \n" ;
    std::cout << "\n";
        
}
void playermove(char *spaces,char player){
    int number;
    do
    {
        std::cout << "enter a spot u want to play in (1-9)!\n >> ";
        std::cin >> number;
        number --;
        if (spaces[number] == ' ')
        {
            spaces[number] = player ;
            break;
        }
        
    } while ( ! (0 < number) || !(number < 8));
    
}
void computermove(char *spaces,char computer){
    int number;
    srand(time(0));
    while (true)
    {
        number = rand()%9;
        if (spaces[number]==' ')
        {
            spaces[number] = computer;
            break;
        }
        
    }
    
}
bool checkwinner(char *spaces,char player) {
    if (spaces[0] !=' ' &&spaces[0]==spaces[1] && spaces[1]==spaces[2])
    {
        spaces[0] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else if (spaces[3] !=' ' &&spaces[3]==spaces[4] && spaces[4]==spaces[5])
    {
        spaces[3] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else if (spaces[6] !=' ' &&spaces[7]==spaces[8] && spaces[8]==spaces[9])
    {
        spaces[6] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else if (spaces[0] !=' ' &&spaces[0]==spaces[4] && spaces[4]==spaces[8])
    {
        spaces[0] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else if (spaces[2] !=' ' &&spaces[2]==spaces[4] && spaces[4]==spaces[6])
    {
        spaces[2] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else if (spaces[0] !=' ' &&spaces[0]==spaces[3] && spaces[3]==spaces[6])
    {
        spaces[0] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    
    else if (spaces[1] !=' ' &&spaces[1]==spaces[4] && spaces[4]==spaces[7])
    {
        spaces[1] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else if (spaces[2] !=' ' &&spaces[2]==spaces[5] && spaces[5]==spaces[8])
    {
        spaces[2] == player ? std::cout << "u won\n" : std::cout << "u lost\n"; 
    }
    else
    {
        return false ; 
    }
    
    return true;
}
bool checktie(char *spaces){
    for (int i = 0; i < 9; i++)
    {
        if (spaces[i]==' ')
        {
            return false ; 
        }
    }
    std::cout << "IT'S A TIE!\n";
    return true;
}
int main(){
    using std::cout;
    using std::cin;

    char spaces[9] ={' ',' ',' ',' ',' ',' ',' ',' ',' ',};
    char player ='X';
    char computer = 'O';
    bool running = true ;
    drawboard(spaces);
    while (running)
    {
        playermove(spaces,player);
        drawboard(spaces);
        if (checkwinner(spaces,player))
        {
            running = false;
            break;
        }
        else if (checktie(spaces))
        {
            running = false;
            break;
        }
        
        computermove(spaces,computer);
        drawboard(spaces);
        if (checkwinner(spaces,player))
        {
            running = false;
            break;
        }
        else if (checktie(spaces))
        {
            running = false;
            break;
        }
    }
    cout << "thanks for playing";
    return 0 ;
}