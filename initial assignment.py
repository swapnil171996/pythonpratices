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
# Rule to define variables
1.there should not be space in variable name
2.variable name cannot start with numbers
3.variable name cannot contains special characters
'''
#Math operator:- +,-,*,/,//,==,!=,%.**

'''
Python Data Type
1.Numbers
    1).Integer
    2).Float
    3).Complex Number
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
str8= '''
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

print("*"*50)

#########List DataType ##############
'''
-> list is mutabledata type,once it is defined we can change it.
->list can contains all type of data int,float,str,list,tuple,dict,set,boolean.
->list follows positive and negative indexing as like string
->list values are comma seperated.
'''
list1=[3,33.56,'hello',[4,5,7],(3,8,2),{'a':123,'b':234},{4,6,9,2},True,None]
print("list1:",list1,type(list1))
list2=[3,4,8]
list2.append(100)
print(list2)
print(list1[2])
'''
import keyword
print(keyword.kwlist)'''

#['False', 'None', 'True', 'and', 'as',
# 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield']

List3=[2,3,[4,7,8],'d']
print(List3[2]) #[4, 7, 8]
print(List3[2][1])

#################Tuple data type#######################
'''
-> tuple is immutable data type,once it is defined we can not change it.
->tuple can contains all type of data int,float,str,list,tuple,dict,set,boolean.
->tuple follows positive and negative indexing as like string
->tuple values are comma seperated.
->tuple defined with round bracket.
->We should use tuple where the data is fixed,which is not going to change once it is defined.
eg.months in years,days in week,number of alphabates.
->tuple is faster then list in terms of performance
'''

tup1=(4,4,5,'hello',[4,5,6],(4,1,3),{'Name':'John'},{5,7,8,2},True)
print(tup1,type(tup1))

tup2=(2,3,(4,7,8),'d')
print(tup2[2])#(4, 7, 8)
print(tup2[2][1])#7

tup3=tup1+tup2
print(tup3)

##################dictonary data type###############
'''
->dictionary store data in key value pair,each data can be identify by unique key.
->dictionary is mutable data type,we can update the data whenever we want.
->dictionary does not allow duplicate key,the keys are always unique.
->All immutable data type can be key in dictonary,int,float,string,tuple,boolean.
->All type of data can be value in dictionary, int,float,string,list,dictonary.set,boolean.
->dictionary value can be duplicate in the data set.
'''
dict1={'a':123,'b':456}
print(dict1['a'])
dict1['c']=500
print(dict1,type(dict1))

dict1['a']=555
print(dict1,type(dict1))
#add mutable data type as key
'''dict1[[1,2,3]]=444
print(dict1)''' #Typeerror unhashable type 'list'

dict2={}
dict2[123]=[1,4,6]
dict2[45.55]={'a':678,'i':908}
dict2[(6,9,8)]={7,8,9,0}
dict2[True]=34555
print("dict2:",dict2)


#########################Set#######################
'''
-->set only store unique values
-->set can contains only immutable data type int,float,string,tuple,boolean
-->setis mutabledata type'''
set={4,4.6,"kish",(98,9,6,8),False,4,4,4}
print("set:",set)#set: {False, 4, 4.6, (98, 9, 6, 8), 8.9, 'kish'}--remove duplicate
set.add(8.9)
print("set:",set)
##################boolan#################
'''
-->boolean is immutable data type
--?boolean can consider with only values True or False
-->All the conditional output will be consider in boolean always
'''
bool1=True
print("bool1:",bool1)
bool2=False
print("bool2:",bool2)