#include <iostream>
using namespace std;

bool Ransom(string ransomNote, string magazine)
{
    int lettercount[26] = {0};

    for (char c : magazine )
    {
        lettercount[c - 'a']++ ;
    }
    for (char c: ransomNote)
    {
        if (lettercount[c - 'a'] == 0)
        {
            return false ;
        }
        lettercount[c - 'a'] -- ;
    }
    return true ;
    
}

int main()
{
    string ransomNote;
    string magazine;

    cout << "ransomNote: ";
    getline(cin , ransomNote);
    cout << "magazine: ";
    getline(cin , magazine);


    if (Ransom(ransomNote , magazine) == true )
    {
        cout << "true";
    }
    else
    {
        cout << "false";
    }
    
    
    return 0;
}