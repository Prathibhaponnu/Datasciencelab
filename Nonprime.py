print("prathibha 21mca034")
n=int(input("Enter the number of terms:"))
for i in range(1,n):
    for j in range(2,i):
        if(i%j==0):
         print(i)
         break

