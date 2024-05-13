s=input("Enter a word: ")
new_s=""
p=""
for c in s :
    if len(new_s)==0:
        new_s+=c
        p=c
    if c==p:
        continue
    else:
        new_s+=c
        p=c
    print(new_s)

print(s)



while True :
        i=1
        b=("BOM","Bom","BOm","BoM","bOm","bOM","boM")
        
#z=(player , computer)
 #       r=random.choice(z)
  #      print(r)
        if i%5==0:
            computer="computer: bom"
            print(computer)
            continue
        else:
            computer="computer: ",i
            print(computer)
            

        i+=1

