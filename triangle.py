n1=int(input("Enter the first side of triangle:"))
n2=int(input("Enter the second side of the triangle:"))
n3=int(input("Enter the third side of the triangle:"))
if(n1==n2==n3):
    print("triangle is equilateral")
elif((n1==n2!=n3)|(n1!=n2==n3)|(n1!=n3==n2)):
    print("triangle is isosceles")
else:
    print("triangleis scalane")
