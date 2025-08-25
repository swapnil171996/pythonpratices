dict1={"a":123,"b":678,"c":345}

print(dict1)
###add data in dictionary
dict1["d"]=4567
print(dict1)

print(dict1["a"])
print(dir(dict1))

for data in dict1:
    print("data:",data)
    '''data: a
data: b
data: c
data: d

'''
for key, val in dict1.items():
    print("key:",key,"values:",val)
    '''
    key: a values: 123
key: b values: 678
key: c values: 345
key: d values: 4567
    '''
####Add different type of data to dict

dict7={}
dict7[23]=456
dict7[2.5]=80.23
dict7["a"]="hello"
print("dict7:",dict7)  #dict7: {23: 456, 2.5: 80.23, 'a': 'hello'
#dict7[[2,4,6]]=[2,6,8,6] #unhashable type: 'list'

dict7[(3,6,8)]=[3,6,7,8]
print("dict7:",dict7) #dict7: {23: 456, 2.5: 80.23, 'a': 'hello', (3, 6, 8): [3, 6, 7, 8]}

#dict7[{"a":123}]="programmig"
print("dict7:",dict7) #nhashable type: 'dict'

dict7["python"]={"name":"john","email":"jphn@123"}
print("dict7:",dict7)#dict7: {23: 456, 2.5: 80.23, 'a': 'hello', (3, 6, 8): [3, 6, 7, 8], 'python': {'name': 'john', 'email': 'jphn@123'}}


dict7[True]=False
print("dict7:",dict7) #dict7: {23: 456, 2.5: 80.23, 'a': 'hello', (3, 6, 8): [3, 6, 7, 8], 'python': {'name': 'john', 'email': 'jphn@123'}, True: False}

#dict7[{8,9,0}]=788999
print("dict7:",dict7) #unhashable type: 'set'

dict7[45]={6,7,8}
print("dict7:",dict7) #dict7: {23: 456, 2.5: 80.23, 'a': 'hello', (3, 6, 8): [3, 6, 7, 8], 'python': {'name': 'john', 'email': 'jphn@123'}, True: False, 45: {8, 6, 7}}




# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

#### add data to dictionary ####
dict_a={}
dict_a["Name"]="swapnil"
print(dict_a) #{'Name': 'swapnil'}

#### update method:This method update data from dict_b to dict_c
dict_b={"a":123,"b":678,"c":345}
dict_c={"d":321,"e":78,"f":453}
dict_c.update(dict_b)
print(dict_c) #{'d': 321, 'e': 78, 'f': 453, 'a': 123, 'b': 678, 'c': 345}

##### get data from dictionry##########
dict2=dict1.get("b")

print("b is key value:",dict1["b"]) #b is key value: 678
print("c is key value:",dict1.get("c"))#c is key value: 345

dict3=dict1.items()
print(dict3) #dict_items([('a', 123), ('b', 678), ('c', 345), ('d', 4567)])

dict4=dict1.values()
print(dict4) #dict_values([123, 678, 345, 4567])

dict5=dict1.keys()
print(dict5) #dict_keys(['a', 'b', 'c', 'd'])


##############################

dict6=dict1.copy()
print(dict6) #{'a': 123, 'b': 678, 'c': 345, 'd': 4567}


