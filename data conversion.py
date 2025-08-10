###############int conversion#############
a=89
float1=float(78)
print("float1:",float1)# float1: 78.0
v=899
str1=str(v)
print(str1,type(str1),str1[1])#899 <class 'str'> 9

v=0
bool_v=bool(v)
print(bool_v) #False

v1=123
bool_v=bool(v1)
print(bool_v) #True
##int to list conversion is not possible
##int to tuple conversion is not possible
###############float Conversion##############
r=78.90
int1=int(r)
print("int1:",int)#nt1: <class 'int'>

r=79.90
str2=str(r)
print("str2:",r,str2[3]) ##str2: 79.9 9

########str convesion #####
#we cannot convert string into int if it contain character/word
'''
str1="hello"
int2=int(str1)
print(int2,type(int2))'''  #ValueError: invalid literal for int() with base 10: 'hello'

str3="234"
int3=int(str3)
print("int3:",type(int3)) #int3: <class 'int'>

str4="234.90"
float3=float(str4)
print("float3:",type(float3)) #float3: <class 'float'>
'''
str1="hello"
float2=float(str1)
print(float2,type(float2))''' ##ValueError: could not convert string to float: 'hello'

str2="programing"
list3=list(str2)
print("list3:",type(list3),list3[3]) ##list3: <class 'list'> g

str2="Good morning"
tuple3=tuple(str2)
print("tuple3:",type(tuple3),tuple3[3]) ##tuple3: <class 'tuple'> d
'''
str2="Good morning"
dict3=dict(str2)
print("dict3:",type(dict3))''' #ValueError: dictionary update sequence element #0 has length 1; 2 is required

import json
str_f='{"a":78,"n":67,"u":65}'
print(str_f,type(str_f),str_f[2])
data_dict=json.loads(str_f)
print(data_dict,type(data_dict)) #{'a': 78, 'n': 67, 'u': 65} <class 'dict'>

str2="Good morning"
set3=set(str2)
print("set3:",type(set3)) #set3: <class 'set'>

str_b=""
bool_b=bool(str_b)
print("bool_b",bool_b) #bool_b False

str_b="helllo"
bool_b=bool(str_b)
print("bool_b",bool_b) ##bool_b True

######List Conversion#############
##List to int,float ,dict coversion is not possible

list1=['h','k','m',8,9,67]
str4=str(list1)
print("str4:",type(str4),str4[3]) #str4: <class 'str'> '

list1=['h','k','m',8,9,67]
tuple4=tuple(list1)
print("tuple4:",type(tuple4),tuple4[3]) #tuple4: <class 'tuple'> 8
'''
list3=['h','k','m',8,9,67]
dict4=dict(list3)
print("dict4:",type(dict4))''' #ValueError: dictionary update sequence element #0 has length 1; 2 is required

list2=['p','e','r']
list5=[4,9,7]
result=dict(zip(list2,list5))
print("result:",type(result),result)#result: <class 'dict'> {'p': 4, 'e': 9, 'r': 7}

list3=['h','k','m',8,9,67]
set4=set(list3)
print("set4:",type(set4))  #set4: <class 'set'>

list6=[]
bool_l=bool(list6)
print("bool_l",type(bool_l),bool_l) #bool_l <class 'bool'> False

list6=[7,8]
bool_l=bool(list6)
print("bool_l",type(bool_l),bool_l) #bool_l <class 'bool'> True

###############tuple##################

##tuple to int,float ,dict coversion is not possible

tuple1=('h','k','m',8,9,67)
str9=str(tuple1)
print("str9:",type(str9),str9[3]) #str9: <class 'str'> '

tuple1=['h','k','m',8,9,67]
list4=list(tuple1)
print("list4:",type(list4),list4[3]) #list4: <class 'list'> 8
'''
list3=['h','k','m',8,9,67]
dict4=dict(list3)
print("dict4:",type(dict4))''' #ValueError: dictionary update sequence element #0 has length 1; 2 is required



tuple8=('h','k','m',8,9,67)
set4=set(tuple8)
print("set4:",type(set4))  #set4: <class 'set'>

tuple6=tuple()
bool_l=bool(tuple6)
print("bool_l",type(bool_l),bool_l) #bool_l <class 'bool'> False

tuple6=(9,8)
bool_l=bool(tuple6)
print("bool_l",type(bool_l),bool_l) #bool_l <class 'bool'> True

################dictionary conversion###############

###dict to int,float conversion is not possible

dict1={"a":45,"g":90,"w":56}
str_d=str(dict1)
print("str_d:",type(str_d),str_d[2]) #str_d: <class 'str'> a

dict1={"a":45,"g":90,"w":56}
list_d=list(dict1)
print("list_d:",type(list_d),list_d[2])#list_d: <class 'list'> w
dict1={"a":45,"g":90,"w":56}
tup_4=tuple(dict1)
print("tup_4:",type(tup_4),tup_4[1])#tup_4: <class 'tuple'> g


dict1={"a":45,"g":90,"w":56}
set_8=set(dict1)
print("set_8:",type(set_8)) #set_8: <class 'set'>

dict1={}
bool_d=bool(dict1)
print("bool_d",type(bool_d),bool_d) ##bool_d <class 'bool'> False

dict1={"e":67,"t":68}
bool_d=bool(dict1)
print("bool_d",type(bool_d),bool_d) ##bool_d <class 'bool'> True

###############setnversion###############

###set to int,float,dict conversion not possible

set2={7,8,9,5,0}
str4=str(set2)
print("str4:",type(str4),str4[1])#str4: <class 'str'> 0

set2={7,8,9,5,0}
list_5=list(set2)
print("list_5:",type(list_5),list_5[2]) #list_5: <class 'list'> 7

set2={7,8,9,5,0}
tuple3=tuple(set2)
print("tuple3:",type(tuple3),tuple3[2])#tuple3: <class 'tuple'> 7

set_u=set()
bool_i=bool(set_u)
print(bool_i,type(bool_i)) #False <class 'bool'>

set_n={9,0}
bool_i=bool(set_n)
print(bool_i,type(bool_i)) #True <class 'bool'>

