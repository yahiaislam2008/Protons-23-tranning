word=input("Entee a word:")
w=[word[0]]
for l in range(1,len(word)):
    if word[l]!=word[l-1]:
        w.append(word[l])


print(*w,sep="")
