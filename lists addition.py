list1=[]
list2=[]
list3=[]
n1=int(input("Enter the number of terms of the first list:"))
n2=int(input("Enter the number of terms of the second list:"))
for i in range(0,n1):
    e1=int(input("Enter the elements of list1"))
    list1.append(e1)
print(list1)
for j in range(0,n2):
    e2=int(input("Enter the elements of list2"))
    list2.append(e2)
print(list2)
if(n1==n2):
   for i in range(0,n1):
      list3.append(list1[i]+list2[i])
print(list3)




