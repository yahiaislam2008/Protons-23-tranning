def counter(word,letter):
    counter=0
    
    for i in range(0,len(word)):
        
        if word[i]==letter:
            counter +=1
    return counter


l=input("letter: ")
w=input("word: ")
#word=input("enter a word: ")
#letter=input("enter a letter: ")

print(counter(w,l))