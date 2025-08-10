'''a=int(input("enter the number:"))
b=int(input("enter the number:"))

if a==b:
    print("number is same")
else:
    print("number is not same")'''

num1=21
if num1%2==0:
    print("number is even")
else:
    print("number is odd")

'''logical operator
>:greater then
<:less then
>=greater then equal to
<=less then equal to
!=equal 

#and
cond1 and cond2
True and False: False
False and True: False
False and False:False
True and True:True

#or 
cond1 or cond2
True or False: True
False or True: True
False or False:False
True or True:True '''

a=90
b=78
c=89

if b>a and b>c:
    print("b is grater number")
else:
    print("b is not a greater number")
#write a python to check given number is divisible by 2 oe3

num2=55
if num2%2==0 or num1%3==0:
    print("the number can divide by 2 or 3")
else:
    print("the number can not divide by 2 or 3")

marks=int(input("enter the marks:"))
if 30< marks<40:
    print("pased with 3rd grade")
elif 40<marks<50:
    print("passed with2nd grade")
elif 50<marks<60:
    print("passed with 1st grade")
else:
    print("Marks value should between 10-100")

round1="pass"
round2="pass"
round3="pass"
if round1=="pass":
    print("1st round is cleared")
    if round2=="pass":
        print("2nd round is cleared")
        if round3=="pass":
           print("congrulation you are placed")
        else:
            print("3rd round is failed")
    else:
        print("2nd round is failed")
else:
    print("1st round is failed")

#python program to check given value is available in the list or not
list1=[8,9,7,4,"k","u","y"]
var1='k'
if var1 in list1:
    print("value is available in the list")
else:
    print("value is not available in the list")

#simple ifcondition with true or false
p=True
if p:
    print("p has true value")
else:
    print("p has false value")

#is not condition with if

#q=[4,7,8,9,0]
q=None
if q is not None:
    print(q)
else:
    print("q has none value")

#Write a python program to check given word is available in the string

str1="good morning ,hope you are doing good"
word="good"

if word in str1:
    print("Word is available in the string")
else:
    print("Word is not available in the string")

num7 = 99
result1= "even number" if num7%2==0 else "odd number"
print("result1",result1)

#write program for calculator #while True:--> to run program infinite loop
print("please select option\n""1. Addition \n"
"2.Multiplication \n"
"3.Subtraction \n"
"4.Divide")

choise=int(input("please enter your choice"))
var1=int(input("please enter your value1"))
var2=int(input("please enter your value2"))

if choise==1:
   print("addition:",var1+var2)
elif choise==2:
    print("multiplication:",var1*var2)
elif choise==3:
    print("sutraction:",var1-var2)
elif choise==4:
    print("divide:",var1/var2)
else:
   print("enter the correct choise number")
