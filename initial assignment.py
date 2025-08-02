a=50
print(a)
address_a=id(a)
print("address of a:",address_a)

p=60
q=60
r=60
print("address of p:",id(p))
print("address of p:",id(q))

#assign multiple variable and different at time
x,y,z=50,60,70
print("value of x:",x)

a=b=c=70
'''
# Rul to define variables
1.there should not be spac in variable name
2.variable name cannot start with numbers
3.variable name cannot contains special characters
'''
#Math operator:- +,-,*,/,//,==,!=,%.**

'''
Python Data Type
1.Numbers
    1).Integer
    2).Float
    3).Complx Number
2.Sequential
    1.String
    2.List
    3.Tuple
3.Dictionary
4.Set
5.Boolean
'''
###############Integer Data Type ###############
var1=100
print(type(var1))
var2=200789098899
print(type(var2))
var3=-4567890000
print(type(var3))

############Float Data type##############
var1=100.560
print(type(var1))
var2=20078.9098899
print(type(var2))
var3=-45678.90000
print(type(var3))
var4=0.0
print(type(var4))

############ Complex data type ##############
data=10+20j
print(data,type(data))
print("real value",data.real,type(data.real))
print("imaginary value",data.imag,type(data.imag))

data2=40+20j
data3=data+data2
print("data3:",data3)

#################String###########
str1=''
str2="H"
str3="good morning"
str4='My name is "Swapnil"'
str5="My country name is 'INDIA'"
str6='''
There's always room for debate when creating a "top 100" list, 
and let's face it, fame is a pretty fickle thing. 
It changes over time. But that said, 
we did our best to use available objective data in putting together
'''
str7='''
1.There's always room for debate when creating a "top 100" list, 
2.It changes over time.
'''
str8='''
There's always room for debate when creating a "top 100" list, \
and let's face it, fame is a pretty fickle thing.\ 
It changes over time. But that said, \
we did our best to use available objective data in putting together\
'''
str9="1.Apple\n"\
     "2.Banana \n"

print("str1:",str1,":",type(str1))

print("str2:",str2,":",type(str2))

print("str3:",str3,":",type(str3))

print("str4:",str4,":",type(str4))

print("str5:",str5,":",type(str5))

print("str6:",str6,":",type(str6))

print("str7:",str7,":",type(str7))

print("str8:",str8,":",type(str8))

print("str9:",str9,":",type(str9))

#indexin in the string
str_a="Python"
'''
0 1 2 3 4 5   +indexing
P Y T H O N
-6 -5 -4 -3 -2 -1 -indexing
'''
print(str_a[0])
print(str_a[-6])

str_b="Hello"
print(str_b[2])
print(str_b[-4])

str_c='good morning'
print("length of str_c",len(str_c))

str_f=str_b+" "+str_c
print("str_f",str_f)





