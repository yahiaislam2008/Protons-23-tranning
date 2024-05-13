a=int(input("Enter angle measure"))
b=int(input("Enter angle measure"))
c=int(input("Enter angle measure"))

def check_triangle(a,b,c):
    if a!=0 and b!=0 and c!=0 and (a+b+c)== 180:

        if a==b and a==c and b==c:
            return "the triangle is Equilateral"

        elif (a+b)==c or (a+c)==b or (b+c)==a:    
            if a==b  or a==c or b==c:
                return "the triangle is Isosceles and the triangle is a Right Angled"
            elif a!=b and a!=c and b!=c:
                return "the triangle is Scalene and the triangle is a Right Angled"
            
            
        elif a!=b and a!=c and b!=c :
            return "the triangle is Scalene"
        
        else:
            return "the triangle is Invalid"
        

print(check_triangle(a,b,c))
        