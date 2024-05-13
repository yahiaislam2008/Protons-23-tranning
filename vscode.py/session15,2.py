listnum=[1,2,7,9,10,11,33,43,99]
print(listnum)
number=int(input("Enter a number: "))
def binarysearch(arr,start,end,number):
    big =0 
    while start<= end:
        mid =start + (end - start) //2
        if start == number :
            big+=1
            return big
        elif mid == number :
            big+=1
            return big
        elif end == number :
            big+=1
            return big
        else:
            start= mid +1
            end= mid -1
    return -1

result=binarysearch(listnum,0,len(listnum)-1,number)
if result !=-1:
    print("her is your number: ",result)
else:
    print("there!!?")