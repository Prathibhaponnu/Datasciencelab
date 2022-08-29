print("prathibha21mca034")
str=input("Enter a string:")
print(str)
vowels='aeiou'
print("Count of vowels in the string")
count={}.fromkeys(vowels,0)
for i in str:
    for j in count:
        if(i==j):
           count[j]=count[j]+1
print(count)
