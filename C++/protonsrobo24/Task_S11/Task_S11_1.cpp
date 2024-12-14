#include <iostream>
#include <algorithm> 
using namespace std;

bool palindrome(string sentence ){
    
    string str = ""; 
    for (char c : sentence){ 
        if (isalnum(c)) 
            str += tolower(c); 
    } 
    string reverse_str = str; 
    reverse(reverse_str.begin(), reverse_str.end()); 
    return str == reverse_str;
    
}



int main(){
    string sentence ;
    

    cout << "\n>> ";
    getline(cin  , sentence) ;
    

    if (palindrome(sentence) == true)
    {
        cout << "true" ;
    }
    else
    {
        cout << "false" ; 
    }
    
    

    return 0 ;
}