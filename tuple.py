tup1=(4,6,8,2,"hello",(4,6,7),[5,1,4])
print(tup1)  #(4, 6, 8, 2, 'hello', (4, 6, 7), [5, 1, 4])

print(tup1[4]) #hello
print(tup1[5][2]) #7

print(tup1[6][::-1]) #[4, 1, 5]
print(tup1[4][::2]) #hlo
print(tup1[1::2]) #(6, 2, (4, 6, 7))
print(f"{tup1[4][0]*2}{tup1[4][1:-1]}{tup1[4][-1]*2}")

#reverse the data in tuple
tup2=(3,5,7,1,8)
print("revered values:",tup2[::-1])#revered values: (8, 1, 7, 5, 3)

##########Apply loop on tupl values#############
tup3=(5,8,9,12,34,56)
for val in tup3:
    print(val)

for i in range(len(tup3)):
    print(i,tup3[i])

##########Methods in tuple############

print(dir(tuple)) #'count', 'index'

#Index method:This method return the index position of specific element
tup4=('a','b','c','p','q','r','a','b','a')
print("Index position of c:",tup4.index("c")) #Index position of c: 2

#count method:This method number ofoccurence of any values
print("count of a:",tup4.count("a")) #count of a: 3

tuple5=(4,15,6,1,7,34,23)
print("Max values:",max(tuple5)) #Max values: 34
print("Min values:",min(tuple5)) #Min values: 1
print("Sum values:",sum(tuple5)) #Sum values: 90

#########################################################
#write a python to create dict output where first tuple is keys and second is values

tup_a=('a','b','c','d')
tup_b=(123,567,786,456)
dict_a={}

for i in range(len(tup_a)):
    dict_a[tup_a[i]]=tup_b[i]

print(dict_a) #{'a': 123, 'b': 567, 'c': 786, 'd': 456}

#Write a python program to find out all values  which are prime in the given tuple values.

tup1=(4,7,1,8,21,23,29)
#output=[7,23,29]

output=[]
for i in tup1:
    if i > 1:
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            output.append(i)
    else:
        pass
print("output:",output)

#2 Write a python program to factorial of given values
tup2=(4,5,3,7)
#output=[24,120,6,729]
output1=[]

for i in tup2:
    fact = 1
    for j in range(1 ,i + 1 ):
        fact*=j
    output1.append(fact)
print("output1:",output1)


tup1=(4,7,1,8,21,23,29,13)
#output=[7,23,29]

out=[]

for i in tup1:
    if i>1:
        count=0
        for j in range (2,i):
            if i%j==0:
                count+=1
        if count==0:
            out.append(i)

print("out",out)



tup2=(4,5,3,7)
#output=[24,120,6,729]
outp=[]

for i in tup2:
    fact=1
    for j in range(2,i+1):
        fact=fact*j
    outp.append(fact)
print(outp)

#Fibonacci sequence
a=0
b=1

for i in range(10):
    print(a)
    a,b=b,a+b


