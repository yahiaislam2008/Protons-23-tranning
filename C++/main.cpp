# include <iostream>
#include <vector> //for typedef
#include <cmath> //for more math operation
#include <ctime> //for randome numbers,not real randome numbers but it is ok
// std::endl = \n
/*
gitline is for strings input if there is spaces
double (for decimal number)
char (single character)
typedef for idenidfe any thing (nickname)
u can convert to any dataa type by doing this (value=(int) x)
for input u use (cin >> (.....))
if there is a string that have spaces u can use the function (getline())
for new line in getline(std::ws)
there is a funcation called max to get the greter value
(min) for the minimum between values
(pow) for power nums
(sqrt)(abs)(round):down(ceil):up(floor)
https://cplusplus.com/reference/cmath/

switch is like if but easy to read it islike this
switch (){
    case 1 ;
     somthing;
     breke;
    defaulte;
}
ther is ternary oprator ?: = replacement to an if/else statement
condition ? expression1 :expresion2 -> use it lke this

&& = (and)=check of two conditions are true 
|| = (or) =check of one conditions are true 
! = reverse = (ex) -> true to false and false to true or not true

length and empty and clear and append and at 
and insert and find and erase (for string functions)

to make a funcation use void and type it from up to down
or u can declaret then ucan write it anywhere in the code
u have to write the data type of the parameters
if u are going to return a value u should make the data type
of the funcation is the same

u can make a varibale global by writting it out the main and any function 
and if u want to use it and there is same varibale use this (::)
ex: 
value =5
main(){
    value =2
    cout << :: value ; u have just used the globale value (value =5)
}

arrays: 
it is typed like this:
datatype value[] = {varibale,varibale};
if u want to print it u can printed by it's index : (cout << value[ndex])
arrays should be the same datatype
sizeof()= determines the size in bytes of a:
          variable, data type, class, objects, etc.

foreach loop = loop thaat eases the traversal over an
               iterable data set

in a funcation if u was looking for somthing so u can (return -1) that means that i didn't found 

fill(the adress , end ,value)

memory address = a location in memory where data is stored
a memory address can accessred with & (address of operator)
hexadecimal -> decimal (Rapidtables)

const parameter = parameter = parameter that is effectively read-only 
                  code is more secure & conveys intent
                  useful for references and pointers

pointers = variable that stors a memory address of another varibale 
           somtimes it's easier to work with an address
& address operator
* dereference operator


dynamic memory = memory that is allocated after the programe
                 is already compiled & running .
                 use the 'new' oprerator to allocate
                 memory in the heap rather than the stack
                 useful when we don't know how much memory
                 we will need. makes our programs more flexible,
                 especially when accepting user input.


function template = describes what a function looks like .
                    can be used to generate as many overloaded functions 
                    as needed , each using different data type  
*/
// typedef std::vector<std::pair<std::string,int>> parelist_t ; //ex 
// typedef std::string str ; //ex | -> use it
// using str = std::string ; //ex | -> use it

// double square(double lenthe){ //i wrote double because we are going to return a duoble
//     double result = lenthe * lenthe; 
//     return result ;
// }

// double totalprice(double prices[] , double size){
//     double total=0 ;
//     for (int i = 0; i < size; i++)
//     {
//         total += prices[i] ;
//     }
    
//     return total;
// }

// int searcharray(double nums[],int size , double num){
//     for (int i = 0; i < size; i++)
//     {
//         if (nums[i]==num)
//         {
//             return i ; 
//         }
//     }
//     return -1;
// }


// void sort(int nums[],int size){
//     int temp ;
//     for (int i = 0; i < size-1; i++)
//     {
//         for (int j = 0; j < size-i-1; j++)
//         {
//             if (nums[j]>nums[j+1])
//             {
//                 temp = nums[j];
//                 nums[j] = nums [j+1];
//                 nums[j+1]=temp;
//             }
            
//         }
        
//     }
    
// }

// void swap(std::string &y , std::string &x){
//     std::string temp;
//     temp =y ;
//     y=x;
//     x=temp ;
// }

//function template
// template <typename T , typename U >
// auto max(T y , U x){ // T as a thing , auto will return the type auto
//    return (x > y) ?  x: y ;  
// }


//struct 
struct Student
{
    std::string name ;
    double gpa ;
    bool enrolled = true ;
};

int main(){
    using std::cout;
    using std::cin;
    

    // std::string name;
    // cout << "what's yourname:  ";
    // getline(cin  , name) ;
    // cout << "hello " << name ;
    //char x =14 ; //ascii table
    // std::cout << (char)100;
    // double x =(int) 88.098 ;
    // std::cout <<x;
    // double students = 50 ;
    // students += 5 ;//= students+5
    // students ++;//= students +1
    // students -=2 ; //= students -2
    // students --; //= students -1
    // students /=5 ;//= students /5
    // students *= 2; //= students *2
    // std ::cout << students << "\n";
    // parelist_t parelist;
    // using namespace std ; // use it 
    // using std::cout;
    // using std:: string;  //this safe
    // string name ="yahia";
    // cout << "hello "  << name << "\n";
    // cout << "al daka 7lwa" << endl; 
    // cout << "kygjgjgjh";

    // double a ;
    // double b ;
    // cout << "enter side a: ";
    // cin >> a;
    // cout << "enter side b: ";
    // cin >> b;
    // cout << "c size = " << sqrt((pow(a,2)+pow(b,2))) ;

    // int grade =90 ;
    // 70 <= grade ? cout << "you passed" << '\n' : cout << "you failed" << '\n';
    // cout << (70 <= grade ?  "you passed" :  "you failed" )<< '\n';

    // int num ;
    // do{
    //     cout<< "enter a positive num: ";
    //     cin >> num ;
    // }while(num <0);
    // cout<<"The num is: " << num;

    // for (int i = 1; i <= 3; i++)
    // {
    //     cout << "oskfsd;lk\n" ;
    // }

    /*
    u can use loop in loop like this 
    ex:
    for (int i = 1; i <=5; i++)
    {
        for (int j = 1; j <= 15; j++)
        {
            cout << j ;
        }
        cout << '\n';
        cout << "hello\n";
        
    }
    \

    */
    
    // srand(time(0));
    //     int num = (rand() % 5)+1; //the % is the range u can generate from randome number
    // cout << num;

    // int num ;
    // srand(time(0));
    // int guess = rand() % 50 +1 ;
    // int tries; 
    // do
    // {
    //     cout<< "enter a number between (1-50): ";
    //     cin >> num ;
    //     tries ++;
    //     if (num > guess)
    //     {
    //         cout << "this num is bigger\n" ;
    //     }
    //     else if (num < guess)
    //     {
    //         cout << "this num is lower\n";
    //     }   
    // } while (num != guess);
    // cout << "u got it in: "<<tries<<" tries";

    // double lenthe = 5 ;
    // cout << (square(lenthe));

    // std :: string cars[] = {"kia","shev","skoda"}; //if u want to declare it later u should set yhe size of indexs
    // cars[2]="camero"; //if u want to change somthing in the array do this
    // cout << cars[1]<<'\n';

    // std::string name = "aiafsiso" ;
    // cout<< sizeof(name) << "bytes\n";

    // std :: string cars[] = {"kia","shev","skoda","jhljlj"};
    // int len = sizeof(cars)/sizeof(std :: string);
    // for (int i = 0; i <=len  ; i++)
    // {
    //     cout << cars[i] << "\n";
    // } //it isnot flexable
        
    // std :: string cars[] = {"kia","shev","skoda"};
    // for(std :: string car : cars){
    //     cout << car << "\n";
    // }//foreach loop is more flexable

    //to pass a array to a funcation u have to pass the address of the aray and it the size of the aray
    // double prices[] = {2,4,24};
    // double size = sizeof(prices)/sizeof(prices[0]);
    // double total = totalprice(prices,size);
    // cout << total << "\n";

    // double nums[]={1,2,3,45,5,7,8};
    // double num ;
    // double size = sizeof(nums)/sizeof(nums[1]);
    // cout << "emter the number u want to search it: \n";
    // cin >> num;
    // int index = searcharray(nums,size,num);
    // if (index == -1)
    // {
    //     cout  << "the num u searched for is not found";
    // }else
    // {
    //     cout << "the number u serched for is on " << index ;
    // }
    
    // //bubble sort
    // int nums[]={323,16,13234,4,6,23,1,3};
    // int size  = sizeof(nums)/sizeof(nums[1]);
    // sort(nums,size);
    // for (int num : nums)
    // {
    //     cout << num << "  ";
    // }


    // int size =100;
    // std :: string cars[size] ;
    // fill( cars, cars+(size-60), "kia");
    // fill(cars+(size-60) , cars +size,"chev");
    // for (std::string car : cars)
    // {
    //     cout << car << "\n";
    // }
    // int size =150;
    // std :: string cars[size] ;
    // fill( cars, cars+(size/3), "kia");
    // fill(cars+(size/3) , cars +(size/3)*2,"chev");
    // fill(cars +(size/3)*2,cars+size,"chery");
    // for (std::string car : cars)
    // {
    //     cout << car << "\n";
    // }

    // //fill with input
    // std::string foods[5];
    // int size =sizeof(foods)/sizeof(foods[1]);
    // std::string temp ;
    // for (int i = 0; i < size; i++)
    // {
    //     cout << "enter a food u like or q to Quit #" << i+1 << ": ";
    //     std::getline(cin,temp);
    //     if ("q"==temp)
    //     {
    //         break;
    //     }
    //     else
    //     {
    //         foods[i]=temp;
    //     }   
    // }
    // cout << "u like the following food:\n";
    // for (int i = 0; !foods[i].empty(); i++)
    // {
    //     cout << foods[i] << "\n";
    // }
    
    // std::string cars [3][3] = {{"mustang","escape","f-150"},
    //                            {"corvette","equinox","silverado"},
    //                            {"challenger","durango","ram1500"}};
    // int size = sizeof(cars)/sizeof(cars[0][0]);
    // for (int i = 0; i < size; i++)
    // {  
    //     for (std::string car:cars[i])
    //     {
    //         cout << car << "\n";
    //     }
    // }
    // int row = sizeof(cars)/sizeof(cars[0]);
    // int column = sizeof(cars[0])/sizeof(cars[0][0]);
    // for (int i = 0; i < row; i++)
    // {
    //     for (int j = 0; j < column; j++)
    //     {
    //         cout << cars[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    
    // std::string name ="yahia";
    // int num =1;
    // bool student =true ;
    // cout << &name << "\n";
    // cout << &num << "\n";
    // cout << &student << "\n";

// pass by value
    // std::string y ="yahia";
    // std::string x = "yassen";
    // std::string temp;
    // temp =y ;
    // y=x;
    // x=temp ;
    // cout << y << "\n";
    // cout << x << "\n";
//pass by reference
    // std::string y ="yahia";
    // std::string x = "yassen";
    // swap(y,x);

    // cout << y << "\n";
    // cout << x << "\n";

//pointer     
    // std::string name = "yahia";
    // int age =16;
    // std::string pizzas[5] = {"pizza1","pizza2","pizza3","pizza4","pizza5"};
    // std::string *pname = &name;
    // int *page = &age ;
    // std::string *pPizzas=pizzas;//we did not use & becase it is already an address
    // cout << *pname << "   " << name << "\n";
    // cout<< *page << "   " << age << "\n";
    // cout << pPizzas << "\n";
    
//null pointer
    // int *pointer = nullptr;
    // int x = 3121;
    // pointer = &x;
// if u want to check the pointer  
    // if (pointer == nullptr)
    // {
    //     cout << "the pointer was not assigned";
    // }
    // else
    // {
    //     cout << "the pointer was assigned\n";
    //     cout << *pointer;
    // }
    
//dynamic memory:
    // int *pnum = NULL ;
    // pnum = new int ; // if u did use new u should use delete because it will case memory leak
    // *pnum =21;
    // cout << "address: "<<pnum<<'\n';
    // cout<< "value: "<<*pnum<<'\n';
    // delete pnum ;

    // char *pGrades= NULL;
    // int size ;
    // cout << "enter the number of grades u had: ";
    // cin >> size;
    // pGrades = new char[size];
    // for (int i = 0; i < size; i++)
    // {
    //     cout << "enter your grade #" << i+1 << ": " ;
    //     cin >> pGrades[i];
    // }
    // cout << "your grades is:    ";
    // for (int i = 0; i < size; i++)
    // {
    //     cout << pGrades[i] << " ";
    // }
    // delete[] pGrades;   

    // cout << max(4,2.21)<<"\n";

//struct 
    // Student student1 ;
    // student1.gpa = 4.2 ;
    // student1.name = "yahia";
    // cout << student1.name << '\n';
    // cout << student1.gpa << '\n';
    // cout << student1.enrolled << '\n';

    return 0;
}