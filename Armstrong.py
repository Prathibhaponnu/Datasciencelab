lower=int(input("Enter the lower limit:"))
upper=int(input("Enter the upper limit:"))
for num in range(lower,upper+1):
    sum=0
    temp=num
    while temp>0:
        dig=temp%10
        sum=sum+dig**3
        temp=temp//10
        if num==sum:
          print(num)




