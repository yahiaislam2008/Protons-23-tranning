n=int(input("Enter Length of the side: "))
x=int(input("Enter Length of the side: "))
z=int(input("Enter Length of the side: "))
def check_triangle(n,x,z):
    
    if x==n==z:
        return "Equilateral"
        
    elif (x==z and x==n) or (z==x and z==n) or (n==z and n==x):
            y=int(input("Enter angle measure: "))
            c=int(input("Enter angle measure: "))
            o=int(input("Enter angle measure: "))
            if y+c+o==180:
                if y==c+o :
                    return "the triangle Isoscelesy and y is a right angle "
                elif c==y+o:
                    return "the triangle Isoscelesy and c is a right angle"
                elif o==y+c:
                    return "the triangle Isoscelesy and o is a right angle"

                else:
                    return "the triangle Isoscelesy"
        
    elif x!=z!=n: 
        return "Scalene"
        
    

   
    
    else :
        return "Invalid"
    
    
print(check_triangle(n,x,z))