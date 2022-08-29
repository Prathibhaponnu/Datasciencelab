print("prathibha21mca034")
a=[]
n1=int(input("Enter the number of terms:"))
print("Enter the terms:")
for i in range(n1):
    b=[]
    for j in range(n1):
        num=int(input())
        b.append(num)
    a.append(b)
print(a)
print("Display matrix elements:")
for i in range(n1):
    for j in range(n1):
        print(a[i][j],end=" ")
    print()
c=[]
n2=int(input("Enter the number of terms:"))
print("Enter the terms:")
for i in range(n2):
    d=[]
    for j in range(n2):
        num=int(input())
        d.append(num)
    c.append(d)
print(c)
print("Display matrix elements:")
for i in range(n2):
    for j in range(n2):
        print(c[i][j],end=" ")
    print()
print("matrix sum is:")
for i in range(0,n1):
    result=[]
    for j in range(0,n2):
        r=a[i][j]+c[i][j]
        result.append(r)
    for r1 in result:
       print(r1)









