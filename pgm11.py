def bsort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
list1=[]
n1=int(input("Enter the number of terms of list1"))
print("enter the terms:")
for i in range(0,n1):
    e1=int(input())
    list1.append(e1)
print("unsorted list:",list1)
print("sorted list",bsort(list1))



