"""
properties:
--> list is mutable data type
-->list is dynamic
-->list can contains all type of data,int,float,string,list,tuple,dict,set,boolean
-->list follows positive and negative indexing
-->list values are comma seperated values
"""
list_a=[4,5,7.8,"hello",[4,6,7],(2,6,8),{"a":123,"b":456},True,{4,7,8}]
print(list_a)
#get value with indexing

print(list_a[3])#hello
print(list_a[-4][-1]) #8

list_b=[4,5,7.8,"hello",[4,6,7,[4,6,[12,56]]],(2,6,8),{"a":123,"b":456},True,{4,7,8}]
print(list_b[4][3][2][1]) #56

#apply loop on the list value
list_c=[5,7,9,2,15]
for val in list_c:
    print(val)
print()
#apply loop with index position
list_c=[3,7,1,8,11,33]
for i in range(len(list_c)):
    print(i,list_c[i])

###############Slicing in list #############
list_d=[3,6,8,"a","b","c","hello","Python"]
print(list_d[4:7])  #['b', 'c', 'hello']

for i in range(len(list_d)):
    print(i,list_d[i])

print(list_d[-2:-7:-1]) #['hello', 'c', 'b', 'a', 8]
print(list_d[1::2])#[6, 'a', 'c', 'Python']
print(list_d[::2]) #[3, 8, 'b', 'hello']
print(list_d[::-2]) #['Python', 'c', 'a', 6]
print(list_d[::-1])# reverse list #['Python', 'hello', 'c', 'b', 'a', 8, 6, 3]

print(dir(list))
'''
[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
#####Add data to the list###########
#append() method:this method add data at end of the list.
list_f=[4,5,6,7,2,8]
list_f.append(100)
list_f.append(50)
list_f.append([7,8,9])
print("list_f:",list_f) # list_f: [4, 5, 6, 7, 2, 8, 100, 50, [7, 8, 9]]

#insert() method:this method add data to list atspecific index position.

list_h=[3,6,8,1,2,4]
list_h.insert(2,"p")
list_h.insert(-1,500)
print("list_h:",list_h) #list_h: [3, 6, 'p', 8, 1, 2, 500, 4]

##############extend method: This method combine the data from list1 to list2

list1=[5,8,7,9]
list2=["a","b","c","d"]
list2.extend(list1)
print("list2:",list2) #list2: ['a', 'b', 'c', 'd', 5, 8, 7, 9]

###########list concatenation#############
#list concatenation combine two list and create new list instead of modify the  existing list.
list1=[5,8,7,9]
list2=["a","b","c","d"]
list3=list1+list2
print(list3) #[5, 8, 7, 9, 'a', 'b', 'c', 'd']

#multiply list values###
list_t=[4,7,2]
list_f=list_t*10
print("list values:",list_f) #list values: [4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2]

################remove data from list############
#remove() method:thismethod will remove specific value the list and does not return it.
list_y=[5,7,8,5,4,8,9]
list_y.remove(4)
print("list_h:",list_y)  #list_h: [7, 8, 5, 8, 9]
list_y.remove(5)
print("list_h:",list_y) #list_h: [7, 8, 5, 8, 9]
##pop() method:this methodremove data from the list using specific index position and return the value
list_l=[4,6,1,7,2,44,22]
#remove from default index
val=list_l.pop()
print("removed value:",val) #removed value: 22
val2=list_l.pop(3) # index postion-3 i.e 7 will remove from list
print("removed value:",val2) #removed value: 7

#write a python program move data from one list to another list
list_t=[4,6,7,81,14]
list_y=[]
for i in range(len(list_t)):
    val=list_t.pop()
    list_y.append(val)
print(list_t,list_y) #[] [14, 81, 7, 6, 4]

##clear method:this method remove all the data from list
list_w=[3,6,8,12,34,56]
list_w.clear()
print("list_w:",list_w) #list_w: []

###remove data from list using delete function
list_q=[3,6,8,9,89]
del list_q[1:4] #we canthe slicing of the list to remove bunch of values
print("list_q:",list_q) #list_q: [3, 89]

#remove entire list from memory
'''del list_q #this will delete list_q from memory
print("list_q:",list_q)#NameError:name 'list_q"
'''

###############data manupulation in the list###############
#replace the list data
list_p=[4,7,2,8,12]
list_p[0]=100
print(list_p) #[100, 7, 2, 8, 12]

list_p[1:4]=["a","b","c"]
print(list_p) #[100, 'a', 'b', 'c', 12]

############sorting of list data###############

#sort method :this method sort the list data in ascending and descending order.
#and update orginal list

list_r=[4,6,8,1,5,12]
#list_r.sort() # sort the list data in ascending order
#print("list_r:",list_r) #list_r: [1, 4, 5, 6, 8, 12]

list_r.sort(reverse=True) #sort  the list data in descending order
print("list_r:",list_r) #list_r: [12, 8, 6, 5, 4, 1]

###sorted function #######
#sorted function(): this function take list values as input and sort the list
#                    data in ascending and descending order.

list_z = [3,6,1,7,2,8,12]
result1=sorted(list_z)
result2=sorted(list_z,reverse=True)
print("result1:",result1)#result1: [1, 2, 3, 6, 7, 8, 12]
print("result2:",result2) #result2: [12, 8, 7, 6, 3, 2, 1]
print("list_z:",list_z) #list_z: [3, 6, 1, 7, 2, 8, 12]


#######reverse the list data###########
##reverse() method this method reverse the list data and modify the original list
list_v=[5,7,12,80,1,3]
list_v.reverse()
print("list_v:",list_v) #list_v: [3, 1, 80, 12, 7, 5]

##reversed() function :this function will return reverse list values and does
#                       not modify the original list
list_m= [4,7,9,1,5,23]
result=reversed(list_m)
print(list(result)) #[23, 5, 1, 9, 7, 4]
print("list_m:",list_m) #list_m: [4, 7, 9, 1, 5, 23]


print("_"*50)

####################get max,min,sum########
list_a=[4,6,8,2,88,22,45]

print("max value:",max(list_a)) #max value: 88
print("min value:",min(list_a)) #min value: 2
print("sum of value:",sum(list_a)) #sum of value: 175

print("_"*50)
#deep copy and shallow copy #######
#shallow copy
list_a=[3,6,2,7,1,5]
list_b=list_a
list_b.append(100)
list_c=list_b
list_c.append(400)

print("list_b:",list_b) #list_b: [3, 6, 2, 7, 1, 5, 100, 400]
print("list_a",list_a) #list_a [3, 6, 2, 7, 1, 5, 100, 400]
print("list_c:",list_c) #list_c: [3, 6, 2, 7, 1, 5, 100, 400]

##deep copy##
list_p=[4,7,2,8,1,9,23]
list_q=list_p.copy()
list_q.append(200)
print("list_q:",list_q)  #list_q: [4, 7, 2, 8, 1, 9, 23, 200]
print("list_p:",list_p) #list_p: [4, 7, 2, 8, 1, 9, 23]

#####list comprehension #####
list_r=[4,6,2,3,7,1,8,23]
result=[]

#get square of all values
for val in list_r:
    val1=val**2
    result.append(val1)
print(result)       #[16, 36, 4, 9, 49, 1, 64, 529]

result=[val**2 for val in list_r] #[16, 36, 4, 9, 49, 1, 64, 529]
print(result)

result1=[val for val in list_r if val%2==0]
print(result1)#[4, 6, 2, 8]

#nested loop with list comprehension

result3=[(x,y) for x in range(3) for y in ["a","b","c"]]
print(result3)  #[(0, 'a'), (0, 'b'), (0, 'c'), (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

list_n=[4,6,7,1,3,8,24]
even_value=[]

for val in list_n:
    if val%2==0:
       even_value.append(val)
print(even_value) #[4, 6, 8, 24]

list_n=[4,6,7,1,3,8,24]
#result=[(4,'even'),(6,'even'),(7,'odd')]
result4=[(val,'even') if val%2==0 else (val,'odd')  for val in list_n]
print("result4:",result4)  #result4: [(4, 'even'), (6, 'even'), (7, 'odd'), (1, 'odd'), (3, 'odd'), (8, 'even'), (24, 'even')]

###write a python program  tochange reverse each values in given list

list_a=["Hello","Python","Programs"]
#output=['olleh','nothyP','smargorP']

output=[]
for val in list_a:
    output.append(val[::-1])

print(output) #['olleH', 'nohtyP', 'smargorP']

#Write a python program to find out the second-highest number from list

list1=[3,6,12,45,223,56]
#output=56

max_num=0
second_max_num=0

for val in list1:
    if val> max_num:
        max_num = val
    elif val < max_num and val > second_max_num:
        second_max_num=val

print("max_num:",max_num) #max_num: 223
print("second_max_num:",second_max_num) #second_max_num: 56



