num1=10
num2='20'
#print("addition of values :",num1+num2) #TypeError: unsupported operand type(s) for +: 'int' and 'str'




def try_except_programs():
    try:
        num1=10
        num2='20'
        print("addition of values :",num1+num2)
    except Exception as e:
        print(e)
        print("Addiion of integer and string is not allowed")

    print("Good Morning")
try_except_programs()
print()
'''
Step-by-Step Breakdown
1. The try block
- Code inside try: is executed normally.
- If no error occurs, the except block is skipped.
2. The Exception class
- In Python, all errors are represented by classes.
- Exception is the base class for most built‑in errors (like TypeError, ValueError, ZeroDivisionError, etc.).
- By writing except Exception, you catch all common runtime errors.
3. The as e part
- e becomes a reference to the actual error object.
- You can print it, log it, or inspect its attributes.

try:
    x = 10 + "20"   # TypeError
except Exception as e:
    print("Error type:", type(e).__name__)
    print("Error message:", e)
Error type: TypeError
Error message: unsupported operand type(s) for +: 'int' and 'str'
'''

#Explicitly raise exception to stop the program to execute further

def try_except_programs_with_raise():
    try:
        num1=10
        num2='20'
        #print("addition of values :",num1+num2)
    except Exception as e:
        print(e)
        print("Addiion of integer and string is not allowed")
        raise

    print("Good Morning") #This wont executes if any exception occurred.

#try_except_programs_with_raise()
'''
unsupported operand type(s) for +: 'int' and 'str'
Addiion of integer and string is not allowed
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#try-except and else condition
def try_expect_else_condition():
    try:
        num1=50
        num2=0
        print("Division of values:",num1//num2) #integer division or modulo by zero
    except Exception as e:
        print(e)
    else:#else condition only executes when there is no exception
        print("Divide operation is successfully")

#try_expect_else_condition() #integer division or modulo by zero

def try_expect_else_condition1():
    try:
        num1=50
        num2=2
        print("Division of values:",num1//num2)
    except Exception as e:
        print(e)
    else:#else condition only executes when there is no exception
        print("Divide operation is successfully") #Divide operation is successfully,Division of values: 25

try_expect_else_condition1()
#try_except_else_condition()

#try-except and finaly block

def try_exception_finally():
    try:
        num1=10
        num2=50
        num3='40'
        print("addition of numbers",num1+num2+num3)
    except Exception as e:
        print(e)
    #finally block always going to excute,even there is exception or no exception
    finally:
        print("This edition operation is successful")

#try_exception_finally()

#handle multiple exception for the operation:

def math_operations_with_multiple_exception():
    try:
        num1=10
        num2=20
        num4=30
        print("addition of numbers",num1+num2)
        division=num4/0
        print("Division error Msg:",division)
    except ZeroDivisionError:
        print("Number can not divide by zero")
    except Exception as e:
        raise
        print(e)

    '''except TypeError as e:
        print(e)
        print("Addiion of integer and string is not allowed")'''
    '''except Exception as e:
        raise
        print(e)'''
    #except assertionError:



#math_operations_with_multiple_exception()

def nested_exception_handing():
    try:
        num1=40
        num2=70
        num3=89

        print("addition of numbers", num1 +num2+num3)
        try:
            assert num1==num2
        except Exception as e:
            print(f"Inner exception {e}")
    except Exception as e:
        print(f"Outer Exception {e}")


nested_exception_handing()


