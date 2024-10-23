#oprators
a=10
b=17
c=14
if a>b and a>c:
    print("A is the biggest")
elif b>c:
    print("B is the biggest")
else:
    print("C is the biggest")
#not oprators
a=23
b=4
c=4
print( a!=b)
print("both are different")
print(b!=c)
#bmi checker
height=float(input("enter your height"))
weight=float(input("enter your weight"))
BMI=weight/height**2
if BMI<=18.4:
    print("you are underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
elif BMI<=34.9:
    print("your are extremely fat")
else:
 print("You are sebely obese")