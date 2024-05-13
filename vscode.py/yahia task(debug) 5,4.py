#a program with a bug can not work or not going to work as expected
#there are three typs of bugs 1.syntax error ,2.run time erorr , 3.logic erorr
#1.syntax error :for ecsample like not putting the : after the if contion
#there is a red  line below the erorr going to show after you delet the : and the reason will pop

if 60>40:
    print("buy it")

#2.run time erorr : when u call a funcation that ever defined when we try to run the code there is an erorr but when we make for her a valiu it's going to work
#so we have to defined



#3.logic erorr : it's a type of erorr that runs but does not work as expectet like loops that counts in the wrong diriction 
#that countions infinty likes the exsample below if the - replaced it with = it's going to be infinty lops

i =10
while i>0:
    i-=1
    print(i)
'''
debugging is a part of programing and in some cases suggest how to fix it and if your code does not
run remeber that your code could have more than 1 bug
and there is a function that called breakpoint() as we are going to see next to the number 
of line that is colored with red as we are going to see in the code below 
'''

x = input("Enter first number : ")
y = input("Enter second number : ")
#delet the # below and run the code
#breakpoint()
#sum = (x* y)
#print(sum)
'''
when we run it as a python file
the code stopped and show us the next line 
output: -> sum = (x* y)
(Pdb) 
after (Pdb) we can type help and it will show us some chioces just like this 
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where
and when we deletthe breakpoint() and we debug the code the code will stop and will tell 
us the problem
'''

def yahia1(number): 
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
#now i am going to click on the redpoint on the lift side of the number of the line below
                numbers[j],numbers[j +1]= numbers[j+1],numbers[j]
#and now the code stopped and there is on top stip over that stips into the next line 
# and there is contiune that start the code starts again in till
# the breakpoint so this it is easier than stip over that we use t manwually
    return numbers


numbers = [4, 3, 12, 1, 5, 17, 12, 2, 6, 9, 10]

#and if i want to put my breakpoint in the line below

print(yahia1(numbers))

'''
so as we see we debuged the code  will go throw the code and will stop so for that there is 
somthing that called step into with it we can run into the function
ant there is somthing that called step over that if u steped into u can get out off the function when i step into
'''