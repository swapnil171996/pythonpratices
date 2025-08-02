
# Python Program to add two integer values.
a=10;
b=20;

print("addition of two:",a+b)

#Python Program to subtract two integer values.
c=30;
d=10;

print("addition of two:",c-d)

#Python program to multiply two numbers.
e=60
f=40

print("multiply of two:",e*f)

#Python program to repeat a given string 5 times.
str1 = "SQATools"
n=5
print("repeat of str1:",str1*n)

#Python program to get the Average of given numbers.
w=40
t=20
y=30

print("average of three number",(w+t+y)/3)

#Python program to get the median of given numbers.

Values=[10,20,30,40,50]
Values.sort()
n=len(Values)
if n%2==1:
    median_value=Values[n//2]
else:
    median_value = (Values[n // 2-1]+Values[n//2])/2
print(f"The median is:{median_value}")

# Python program to print the square and cube of a given number.
num1=9
print("square of the number",num1**2)
print("cube of the number",num1**3)

#Python program to interchange values between variables.

r=10
j=20

j,r=r,j
print("interchange values",j,r)
#Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)

#

y = 2
u = 3
result = y**2+2*u*y+u**2
er=(2+3)**2
print(result == er)
print("(y+u)^2: ",result)
#Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)

t=70
i=80

equal=t**2-i**2
sub= (t-i)*(t+i)
print("subt",sub)
print("euql",equal)

k = 9
l = 8
result = k**2-2*k*l+l**2
er=(k-l)**2
print(result == er)
print("(k-l)^2: ",result)

#Python program to calculate the area of the square.
#Formula : area = a*a
'''s=10
print("area :",s*s)

side = int(input("Enter the side of a square: "))
print("Area of sqaure: ",side**2)

#Python program to calculate the area of a circle.Formula = PI*r*r
r = radius
PI = 3.14

r=12
Pi=3.14

print("area of circle:",Pi*r*r)

r=int(input("Enter the radius of circle"))
Pi=3.14
print("area of circle:",Pi*r*r)

#Python program to calculate the area of a cube.Formula = 6*a*a
a=int(input("Enter the value"))
print("area of a cube",6*a*a)
num = a = 153
rev = 0

while a>0:
    rem = a%10
    print("rem",rem)
    rev = rev +rem**3
    print("rev", rem)
    a= a//10
    print("a", a)

if rev == num:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")


number= int(input("Enter the number"))
length =len(str(number))
temp = number
sum=0
while temp>0:
    digit=temp%10
    print("digit",digit)
    sum+=digit**length
    print("sum", sum)
    temp=temp//10
if sum==number:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")

 #Python program to print the current date in the given format
import datetime
date=datetime.datetime.now()
print (date.strftime (" %Y %b %d "))

#Python program to calculate days between 2 dates

from datetime import date

date_1 = date(2023, 1, 5)
date_2 = date(2023, 1, 22)

result = (date_2 - date_1).days
print ("Number of Days between the given Dates are: ", result, "days")

# program to get the factorial of the given number.
number= int(input("Enter the number"))
fact=1
while number>0:
    fact*=number
    number-=1
print("factorial",fact)

#reverse number--123
number= int(input("Enter the number"))
reverse_number=0
while number>0:
    digit=number%10
    reverse_number=reverse_number*10+digit
    number=number//10
print("the reverse number:",reverse_number)
a, b = 0, 1
count=0
print("the sequence is:",end=' ')
while count < 50:
    print(a,end=" ")
    n2=a+b #1
    a+=1 #1
    a=b #1
    b=n2
    count+=1

#Program to check given number is palindrome or not
n = num = int(input("Enter a number: "))
rev = 0
while n>0:
    rem = n%10
    rev = rev*10+rem
    n = n//10
print("rev_number:",rev)
if num == rev:
    print("Given number is a palindrome number")
else:
    print("Given number is not a palindrome number")
 '''





