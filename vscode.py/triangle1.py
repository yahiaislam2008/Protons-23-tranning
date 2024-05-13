a=int(input("Enter the lenth of the triangle: "))
b=int(input("Enter the lenth of the triangle: "))
c=int(input("Enter the lenth of the triangle: "))
def check_triangle(a,b,c):
        while a+b>=c and a+c>=b and b+c>=a:
            if a==b and a==c and b==c:
                return "the triangle is Equilateral"
            elif a==b :
                return "the triangle is Isosceles"
            elif b==a :
                return "the triangle is Isosceles"
            elif c==a :
                return "the triangle is Isosceles"
            elif (c**2+b**2)==a**2 or (a**2+c**2)==b**2 or (a**2+b**2)==c**2:
                return "the triangle is right angled"
            elif a!=b and a!=c and b!=c:
                return "the triangle is Scalene"
        else:
            return "the triangle is Invalid"
    
print(check_triangle(a,b,c))