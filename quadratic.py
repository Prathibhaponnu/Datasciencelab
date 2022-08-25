print("prathibha21mca034")
import cmath
def find_roots(a,b,c):
  d=((b**2)-4*a*c)
  result=cmath.sqrt(d)
  if d>0:
      print("Real and different roots")
      print((-b+result)/(2*a))
      print((-b-result)/(2*a))
  elif d==0:
      print("same roots")
      print(-b/(2*a))
  else:
      print("complex numbers:")
      print((-b+result)/(2*a),"+i",result)
      print((-b-result)/(2*a),"-i",result)

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if(a==0):
    print("input correct quadratic equation")
else:
    find_roots(a,b,c)

