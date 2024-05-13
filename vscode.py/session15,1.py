listnum=[1,2,7,9,10,11,33,43,99]
print(listnum)
number=int(input("Enter a number: "))
def binarysearch(arr,left,right,number):
    mid =left + (right - left) //2
    while left<= right and left <= mid and mid <=right:
        if arr[mid] == number:
            mid =left + (right - left) //2
            return mid+1
            
        
        elif arr[mid] < number :
            left= mid +1
            mid =left + (right - left) //2

        else:
            right = mid -1
            mid =left + (right - left) //2    
    return -1

result=binarysearch(listnum,0,len(listnum)-1,number)
if result !=-1:
    print("her is your number: ",result)
else:
    print("can not find your number!!?")