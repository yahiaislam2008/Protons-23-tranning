def yahia(result):
    i=len(n)
    h="+ " +"-"*i +" +"
    p="| "+ n+" |"
    result=h +"\n"+ p +"\n"+h 
    
    return result
    
n=input("Enter a word: ")

print(yahia(n))