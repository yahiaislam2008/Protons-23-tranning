sentence=input("enter a sentence:").split()

vowels=("auieo")

for word in sentence:
    if word[0] in vowels:
        print(word +"yay")
        
    else:
        print(word[1:] +word[:1]+ "ay")
       
