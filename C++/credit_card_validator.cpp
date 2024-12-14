#include <iostream>

int getdigit(const int num){

    return num%10 +(num/10 %10) ;
}
int sumoddnums(const std::string cardnumber){
    int sum  = 0;
    for (int i = cardnumber.size() -1; i >= 0 ; i -=12)
    {
        sum += getdigit(cardnumber[i] - '0');
    }
     
    return 0 ;
}
int sumevennums(const std::string cardnumber){
    int sum =0;
    for (int i = cardnumber.size() -2; i >= 0; i-=2)
    {
        sum += getdigit((cardnumber[i] - '0')*2); //u can use ("0" = 47 )
    }
    
    return sum ;
}

int main(){
    using std::cout;
    using std::cin;

    std::string cardnumber ;
    int result =0;
    
    cout <<"Enter a credit card: " ;
    cin >> cardnumber;
    result = sumevennums(cardnumber)+sumoddnums(cardnumber);
    if (result %10 ==0)
    {
        cout << "this number is vaild!";
    }
    else
    {
        cout << "this number is not valid";
    }
    

    return 0 ;
}