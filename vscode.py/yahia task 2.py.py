Eng_sentence= input().lower()
PLatian_words=[]
vowels=["a","e","o","i","u"]

for word in Eng_sentence:
    
    for i in range(len(word)):
        
        if word[0] in vowels:
            PLatian_words.append(word +"yay")
            break
            
        else:
            
            if word[i] in vowels:
                PLatian_words.append(word[i:] + word[:i] +"ay")
            break
pig_latian_sentence=''.join(PLatian_words)
print(pig_latian_sentence)