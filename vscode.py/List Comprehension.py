#Iterating through a string Using for Loop

o_letters=[]

for letter in "hello world":
    o_letters.append(letter)


print(o_letters)

#but to make the code easier we will use List Comprehension
#Iterating through a string Using List Comprehension

i_letters=[letter for letter in "protons"]

print(i_letters)

#Using Lambda functions inside List
#not important
letters=list(map(lambda x:x , 'yahia'))

print(letters)



#Using if with List Comprehension

nums_list=[x for x in range(15) if x%3==0]

print(nums_list)


#Nested IF with List Comprehension

num_list=[y for y in range(50) if y%4==0 if y%2==0]

print(num_list)

#Using if...else With List Comprehension

digits=["even" if i%2==0 else "odd" for i in range(12+1)]

print(digits)

